# General AWS Credentials
aws_access_key_id="##########################################################"
aws_secret_access_key="######################################################"
aws_session_token="############################################################"
aws_userId="##################################################################"

# Redis
redis_ttl = 20*60  #20 minutes

# For Crawlers
bucket_name = "crawled-unprocessed-data"

# For Model Creation and Deployment
model_output_folder = "./model/"
model_file_name = "rss_model.pkl"
corpus_file_name = "corpus.pkl"
metadata_file_name = "metadata.pkl"
top_document_count = 5

# Dynamo-DB Detailsce
table_name = "news_data"

# APIs
get_doc = "http://3.237.13.47/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
