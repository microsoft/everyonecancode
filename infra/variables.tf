variable "STATIC_WEBSITE_URL" {
  description = "The URL of the static website"
  type        = list(string)
  default     = ["https://microsoft.github.io", "http://localhost:3000"]
}

variable "PARTICIPANT_ID" {
  description = "The unique ID of a participant. This is used to customize name of resources created for the participant."
  type        = string
  default     = ""
}
