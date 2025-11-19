from pathlib import Path

if __name__ == "__main__":
    # problem1
 data_dir = "04/data"
 data_dir_path = Path(data_dir).resolve()
 print("===problem1===")
 print(f"data_dir_path : {data_dir_path}")

    # problem2
 print ("===problem2===") 
 file_list = list(data_dir_path.glob("*"))
 for path in enumerate(file_list):
     print(f"file{path[0]} : {path[1]}")

    # problem3
 print("===problem3===")
 