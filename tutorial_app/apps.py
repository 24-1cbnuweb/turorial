from django.apps import AppConfig
import os
import json
import pandas as pd
from django.conf import settings

class MyAppConfig(AppConfig):
    name = 'tutorial_app'

    def ready(self):
        # 서버 시작 시 특정 엑셀 파일 자동 처리
        excel_file_path = os.path.join(settings.MEDIA_ROOT, 'test_data.xlsx')
        if os.path.exists(excel_file_path):
            self.process_excel_file(excel_file_path)

    def process_excel_file(self, excel_file_path):
        # 엑셀 파일 읽기
        excel_data = pd.read_excel(excel_file_path)
        
        # 엑셀 데이터를 JSON 형식으로 변환
        json_data = excel_data.to_json(orient='records', force_ascii=False)
        struct_data = json.loads(json_data)
        
        # JSON 파일 경로 생성
        json_file_path = os.path.join(settings.MEDIA_ROOT, 'output.json')
        
        # JSON 파일로 저장
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(struct_data, f, ensure_ascii=False, indent=2)
        
        print(f'File {excel_file_path} processed and converted to JSON.')