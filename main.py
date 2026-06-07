import os
import requests

def fetch_and_save():
    # 这是一个通用的获取示例
    source_url = "https://example.com/api/data" 
    output_filename = "live.m3u"
    
    try:
        # 发送请求获取数据
        response = requests.get(source_url, timeout=15)
        response.raise_for_status()
        
        # 假设这里经过了您的自定义清洗或逻辑处理
        processed_data = response.text 
        
        # 将结果写入或覆盖到 live.m3u 文件中
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(processed_data)
            
        print(f"成功更新 {output_filename}")
        
    except Exception as e:
        print(f"数据获取失败: {e}")

if __name__ == "__main__":
    fetch_and_save()
