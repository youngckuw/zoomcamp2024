variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-creds.json"
}


variable "region" {
  description = "Region"
  default     = "us-west1"
}


variable "project" {
  description = "Project"
  default     = "datacamp2004"
}


variable "location" {
  description = "Project Location"
  default     = "US"
}


variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}


variable "gcs_bucket_name" {
  description = "My Storage Bucketname"
  default     = "datacamp2004-terra-bucket"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

