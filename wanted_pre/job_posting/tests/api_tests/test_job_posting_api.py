import json
from rest_framework.test import APIClient, APITestCase

from job_posting.models import Company as CompanyModel
from job_posting.models import CompanyCountry as CompanyCountryModel
from job_posting.models import CompanyRegion as CompanyRegionModel
from job_posting.models import Skill as SkillModel
from job_posting.models import JobPosition as JobPositionModel, JobPosting as JobPostingModel

DOES_NOT_EXIST_NUM = -1

class TestJobPostingAPI(APITestCase):
    """
    JobPostingView의 API를 검증하는 클래스
    """

    @classmethod
    def setUpTestData(cls):
        county_for_test = CompanyCountryModel.objects.create(country = "한국")
        region_for_test = CompanyRegionModel.objects.create(region = "서울")
        SkillModel.objects.create(skill_name="python")
        JobPositionModel.objects.create(job_position="개발자직군")
        CompanyModel.objects.create(name="1번회사", country=county_for_test, region=region_for_test)

    def test_post_jobpost(self):
        """
        JobPostView의 post 함수를 검증하는 함수
        case : 정상적으로 작동을 했을 경우
        """
        company_id = CompanyModel.objects.get(name="1번회사").id
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        client = APIClient()
        request_data = {"company" : company_id, "job_position" : job_position_id, "compensation" : 100000, "content" : "회사소개", "skill" :skill_id}

        url = "/job_post/"
        response = client.post(url, data=json.dumps(request_data), content_type="application/json")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["detail"], "새로운 채용공고가 등록이 되었습니다.")

    def test_when_post_jobpost_does_not_exist_company_data(self):
        """
        JobPostView의 post 함수를 검증하는 함수
        case : 모델에 존재하지 않는 PK를 받았을 경우
        """
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        client = APIClient()
        request_data = {"company" : DOES_NOT_EXIST_NUM, "job_position" : job_position_id, "compensation" : 100000, "content" : "회사소개", "skill" :skill_id}

        url = "/job_post/"
        response = client.post(url, data=json.dumps(request_data), content_type="application/json")
        result = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result["detail"], "모델에 존재하지 않는 PK를 받고 있습니다.")
