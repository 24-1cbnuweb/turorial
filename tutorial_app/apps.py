from django.apps import AppConfig
import os
import json
import pandas as pd
from django.conf import settings

class MyAppConfig(AppConfig):
    name = 'tutorial_app'

    def ready(self):
        # 서버 시작 시 특정 엑셀 파일 자동 처리
        domestic_excel_file_path = os.path.join(settings.MEDIA_ROOT, 'Domestic Fruit Data.xlsx')
        if os.path.exists(domestic_excel_file_path):
            self.process_excel_file(domestic_excel_file_path, 1)
        
        imported_excel_file_path = os.path.join(settings.MEDIA_ROOT, 'Foreign Fruit Data.xlsx')
        if os.path.exists(imported_excel_file_path):
            self.process_excel_file(imported_excel_file_path, 2)
            
        frozen_excel_file_path = os.path.join(settings.MEDIA_ROOT, 'Frozen Fruit Data.xlsx')
        if os.path.exists(frozen_excel_file_path):
            self.process_excel_file(frozen_excel_file_path, 3)

        all_excel_file_path = os.path.join(settings.MEDIA_ROOT, 'All Fruit Data.xlsx')
        if os.path.exists(all_excel_file_path):
            self.process_excel_file(all_excel_file_path, 4)
            
    def process_excel_file(self, excel_file_path, num):
        # 엑셀 파일 읽기
        excel_data = pd.read_excel(excel_file_path)
        
        # 엑셀 데이터를 JSON 형식으로 변환
        json_data = excel_data.to_json(orient='records', force_ascii=False)
        struct_data = json.loads(json_data)
        
        # JSON 파일 경로 생성
        if (num == 1):
            json_file_path = os.path.join(settings.MEDIA_ROOT, 'domestic.json')
        elif (num ==2):
            json_file_path = os.path.join(settings.MEDIA_ROOT, 'import.json')
        elif (num ==3):
            json_file_path = os.path.join(settings.MEDIA_ROOT, 'frozen.json')
        elif (num ==4):
            json_file_path = os.path.join(settings.MEDIA_ROOT, 'all.json')    
                
        # JSON 파일로 저장
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(struct_data, f, ensure_ascii=False, indent=2)
        
        print(f'File {excel_file_path} processed and converted to JSON.')