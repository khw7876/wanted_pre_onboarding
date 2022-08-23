from django.test import TestCase
from rest_framework import exceptions

from job_posting.models import Company as CompanyModel
from job_posting.models import CompanyCountry as CompanyCountryModel
from job_posting.models import CompanyRegion as CompanyRegionModel
from job_posting.models import Skill as SkillModel
from job_posting.services.job_posting_service import create_job_post
from job_posting.models import JobPosition as JobPositionModel, JobPosting as JobPostingModel

DOES_NOT_EXIST_NUM = 999
class TestCreateJobPost(TestCase):
    """
    job_posting의 서비스들를 검증하는 클래스
    """

    @classmethod
    def setUpTestData(cls):
        county_for_test = CompanyCountryModel.objects.create(country = "한국")
        region_for_test = CompanyRegionModel.objects.create(region = "서울")
        SkillModel.objects.create(skill_name="python")
        JobPositionModel.objects.create(job_position="개발자직군")
        CompanyModel.objects.create(name="1번회사", country=county_for_test, region=region_for_test)

    def test_create_job_post(self):
        """
        채용공고를 생성하는 service함수 검증 
        case: 정상적으로 작동을 했을 경우
        """
        company_id = CompanyModel.objects.get(name="1번회사").id
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        test_request_data = {"company" : company_id, "job_position" : job_position_id, "compensation" : 100000, "content" : "회사소개", "skill" :skill_id}
        create_job_post(test_request_data)

        self.assertEqual(
            JobPostingModel.objects.all().count(), 1
        )

    def test_when_create_job_post_does_not_exist_company_data(self):
        """
        채용공고를 생성하는 service함수 검증 
        case: 없는 회사 데이터를 입력했을 경우
        """
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        test_request_data = {"company" : DOES_NOT_EXIST_NUM, "job_position" : job_position_id, "compensation" : 100000, "content" : "회사소개", "skill" :skill_id}
        
        with self.assertRaises(exceptions.ValidationError):
            create_job_post(test_request_data)

    def test_when_create_job_post_does_not_exist_jobpost_data(self):
        """
        채용공고를 생성하는 service함수 검증 
        case: 없는 채용포지션 데이터를 입력했을 경우
        """
        company_id = CompanyModel.objects.get(name="1번회사").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        test_request_data = {"company" : company_id, "job_position" : DOES_NOT_EXIST_NUM, "compensation" : 100000, "content" : "회사소개", "skill" :skill_id}
        
        with self.assertRaises(exceptions.ValidationError):
            create_job_post(test_request_data)

    def test_when_create_job_post_does_not_exist_skill_data(self):
        """
        채용공고를 생성하는 service함수 검증 
        case: 없는 사용기술 데이터를 입력했을 경우
        """
        company_id = CompanyModel.objects.get(name="1번회사").id
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id

        test_request_data = {"company" : company_id, "job_position" : job_position_id, "compensation" : 100000, "content" : "회사소개", "skill" :DOES_NOT_EXIST_NUM}
        
        with self.assertRaises(exceptions.ValidationError):
            create_job_post(test_request_data)
    
    def test_when_create_job_post_content_is_over_200_length(self):
        """
        채용공고를 생성하는 service함수 검증 
        case : content 제한수 200을 초과하였을 경우
        """
        company_id = CompanyModel.objects.get(name="1번회사").id
        job_position_id = JobPositionModel.objects.get(job_position="개발자직군").id
        skill_id = SkillModel.objects.get(skill_name = "python").id

        test_request_data = {"company" : company_id, "job_position" : job_position_id, "compensation" : 100000, "content" : str("A"*210), "skill" :skill_id}

        with self.assertRaises(exceptions.ValidationError):
            create_job_post(test_request_data)