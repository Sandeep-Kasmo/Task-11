from extract import *
from transform import *
from connection import *
from load import *

def main():
    #establish connection
    establish_connection()

    #extract data
    first_project=get_data("PythonLearningDB","First_project")

    #print data
    print(first_project.info())

    #apply transformation
    transformed_first_project=transform_data(first_project)
    print(transformed_first_project)
    print(transformed_first_project.info())

    #load the transformed data back to mongodb
    load_to_mongo(transformed_first_project,'PythonLearningDB','transformed_first_project')
    #clsoe the connection
    close_connection()

if __name__=='__main__':
    main()