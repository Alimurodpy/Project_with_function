def log_decarator(func):
    def wrapper(*args, **kwargs):
        
        print(f"[START]", func.__name__, "is running")
        if func.__name__ == "add_product":
            print(f"[INFO] Yangi mahsulot qo'shilish jarayonida:")
            
            result = func(*args, **kwargs) 
            
            print(f"[INFO] Yangi mahsulot qo'shildi. Mahsulot oilasi {args[0]}, mahsulot nomi {args[1]}, miqdori {args[2]}, buy price {args[3]}, sell price {args[4]}, unit {args[5]}")
            return result
        
    return wrapper