

# Use Case Recommender 워크샵
---
2021 년도에 re:Invent에서 새롭게 소개한 `Use Case Recommender` 의 핸즈온을 할 수 있는 워크샵 입니다. 두 개의 지정된 도메인 (1) VIDEO_ON_DEMAND , (2) ECOMMERCE 에서 여기서는 ECOMMERCE 를 다룹니다.

- 현재 (2022.1.3) 공식 예제가 출시가 나오지 않아서, 사용할 데이터의 발견이 쉽지 않아서 기존의 "Retail Demo" 의 Sample 에서 사용한 데이터 세트를 사용하였습니다. 
- 개발자 가이드를 통해서 기능을 구현하였고, 몇 가지 "추천의 결과" 의미를 이해하지 못한 부분이 있습니다. 참고 바랍니다. 
- 현재 "설명" 등이 많이 부족합니다. 추후에 업데이트 하겠습니다.


# 0. 핸즈온 사전 단계
---

- 이벤트 엔진, Cloud Formation 이용: 
    - [핸즈온 준비 필수 단게: Prerequisite](../personalize/0.0.Prerequisite/CF-Prerequisite.md)
- 이벤트 엔진, 수동 설정: 
    - 이벤트 엔진으로 시작을 안 한다고 하면, 이 과정은 생략하세요.
    - [여기](../personalize/0.0.Prerequisite/Prerequisite.md) 를 클릭해서 해주세요.
- SageMaker notebook instance 를 이미 가지고 있는 경우
    - SageMaker notebook instance를 실행하는 Role이 아래 4개의 권한을 꼭 가지고 있어야 합니다. 아래 권한을 추가 해주세요. 참고로 위의 수동 설정에는 아래 4가지 권한을 추가하는 과정이 있습니다. 참고 하세요. (AmazonSageMakerFullAccess, AmazonS3FullAccess, AmazonPersonalizeFullAccess, IAMFullAccess)


# 1. 워크샵을 통해 구현할 내용
---
아래와 같이 4가지의 제공된 Use Case 가 있습니다. 아래 4개 모두를 구현 합니다.
- Most viewed
    - 고객이 항목을 본 횟수를 기반으로 인기 항목에 대한 추천을 받으세요.
- Best sellers
    - 고객이 상품을 구매한 횟수를 기반으로 인기 상품에 대한 추천을 받으세요.
- Frequently bought together
    - 고객님이 지정하신 상품을 기반으로 고객이 함께 자주 구매하는 상품 추천을 받아보세요.
- Customers who viewed X also viewed
    - 지정한 항목을 기반으로 고객이 본 항목에 대한 권장 사항을 가져옵니다.
    


# 2. 데이터 설명
---
아래의 Git에서 인공적으로 생성된 데이터 세트를 사용 함.

- 생선데 데이터 세트를 tar 로 압축하여 현재의 git 에 저장 했습니다. 이를 압축해제 해서 사용합니다.


* Retail Demo Store
    * https://github.com/aws-samples/retail-demo-store




# 3. 노트북 설명
---
* 0.1.Install_Package.ipynb
    - 필요한 파이썬 패키지를 설치 합니다. (Conda-Python3 커널을 사용합니다.)
- 1.1.Prepare_Dataset.ipynb
    - 저장된 데이타를 압축 풀고, 간단한 데이터 탐색을 합니다.
- 1.2.Transform_Dataset.ipynb
    - 퍼스널라이즈에 데이터를 입력하기 위해 데이터를 선택하고, 포맷을 맞게 고칩니다.
- 2.1.Create-Dataset-Group.ipynb
    - 퍼스널라이즈의 "데이터 세트 그룹", "데이터 세트", "데이터 스키마", 데이타 임포트" 를 생성 합니다.
- 3.1.Create_Recommenders.ipynb
    - Recommender 를 생성 합니다.
- 4.1.Get_Recommends.ipynb
    - 위에서 생성한 Recommender 를 통해서 추천을 받습니다.
- 9.1.Cleanup.ipynb
    - 모든 리소스 제거 노트북 입니다.
    




# A. 참고 자료:
---
- Amazon Personalize Developer Guide
    - 공식 개발 문서 가이드 입니다.
    - https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html


- ECOMMERCE datasets and schemas 개발자 가이드
    * https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-datasets-and-schemas.html
    
- AWS Boto3 Python SDK for Personalize
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_recommender


- Amazon Personalize Samples
    - 공식 에제 Git 저장소 입니다.
    - https://github.com/aws-samples/amazon-personalize-samples



