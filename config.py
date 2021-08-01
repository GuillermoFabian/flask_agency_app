# This file should be hidden, to not expose sensitive data
import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# database local conenction params
database_params = {
    "username": "admin",
    "password": "admin",
    "db_name": "test",
    "dialect": "postgresql"
}

# auth0 token that are used for unit_test

auth0_tokens = {

    "assistant": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJxUi11T2Z1OFBjbEUzSDVWd1N1VCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ma29seTY4Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwNmVlYzYyNDU0ZjIwMDZhMjRhYTRmIiwiYXVkIjoiZGlzY29ncmFwaHkiLCJpYXQiOjE2Mjc4NDU0NDksImV4cCI6MTYyNzg1MjY0OSwiYXpwIjoiN3JTUTJNdWd0Vm1lMzRxUFIxN0hSRjlKbW9PaTdHZmEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzaW5nZXIiLCJnZXQ6c29uZyJdfQ.aeRfBVKGtK6CsDyK9_6Bq2UswiiA0Ij6JE1bk7kRLJ0IwY3hP8yA9Fw4Y_K_CLg9doT7sZsB41UxhsjELc9j1MX8pb-Bi_tVV-jcunNCfEQJShhNF_ulPyUa9aUggKmLFC_9UttqoBb_gQMQpzK2R-gNfnib-VmSDZEqXOiI5FKGhHdUVPqoLPOX_KarQ83jkdbWhs-LfRzJo0Q7gSlUawT9dzCoq4ZXneKXaJAKmH-y5X3ohpimb6u_TMuIE9UH1sYkHKHo9YP89UO6rpOpfP-vxLQi1VG-0L3XAnjg59_svXxSM8fwVWzvQGH1kftTN71JS6pQnaWKN-1IUs_geg",
    "manager": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJxUi11T2Z1OFBjbEUzSDVWd1N1VCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ma29seTY4Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwNmVmMDFjNzI0MDUwMDcxYjY3YjdmIiwiYXVkIjoiZGlzY29ncmFwaHkiLCJpYXQiOjE2Mjc4NDUxNjIsImV4cCI6MTYyNzg1MjM2MiwiYXpwIjoiN3JTUTJNdWd0Vm1lMzRxUFIxN0hSRjlKbW9PaTdHZmEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzaW5nZXIiLCJnZXQ6c29uZyIsInVwZGF0ZTpzaW5nZXIiLCJ1cGRhdGU6c29uZyJdfQ.yVu8tskZBhCzJao0ZKAts1b_6eTKAfNNf4uyI7xWPmOOyY9cY4xQCNhAGzX6-snriEuyThtDr4pIbYLro6DksZyhwQk2rTs8G-0CljPzykIULLtMH6ejJ2PGtXdBn39XcSKIc6uesZuMA3Sl-dBG8ZjX4_u-gavUvrBEpjJnxCyJma6JTLLtIAeWsI7Z1aFCfFk0GMM7vCh47UaDmjc8z8q1ji4hTHbnOBf2liXOxJX5H5HKgStjRwV814n4ecdv4Cg5gn-yob28Z-oQTMow2I0bAcbSWX_YEmRTj-b78BXfkos5r7FLUmhnS8Ek1cPGxIU9XFKImvt1AevQmoRMWw",
    "owner": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJxUi11T2Z1OFBjbEUzSDVWd1N1VCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ma29seTY4Mi51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNDE2MDY5NjQ2MTY3ODY3NzMiLCJhdWQiOiJkaXNjb2dyYXBoeSIsImlhdCI6MTYyNzg0MzYyMCwiZXhwIjoxNjI3ODUwODIwLCJhenAiOiI3clNRMk11Z3RWbWUzNHFQUjE3SFJGOUptb09pN0dmYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOnNpbmdlciIsImNyZWF0ZTpzb25nIiwiZGVsZXRlOnNpbmdlciIsImRlbGV0ZTpzb25nIiwiZ2V0OnNpbmdlciIsImdldDpzb25nIiwidXBkYXRlOnNpbmdlciIsInVwZGF0ZTpzb25nIl19.jkm-evoCPGt6ZZ4vN1ZJ03O5C7msY1tvKpvjX1cOXYC0-UKuL1NmCRjXoDzh92DeTVw505JFFG8iO8QEyDLkGkPAUeywboUeEvDBCzD6zscjSro6uy6iEe4Yv5oj-3bbn6Fn4ZOnA-2lJvpspoRqixzh4QmJN8BNa65rOM1oATvX670YD0D9u5ivRvFHl1GTeNfm9AMQfAU3uFQV5m0EptccwnZQgHhbLPor2XbcelKqSyondfhFoxMYNHPIAnG4Bnq7Z86tcIpd55urYn8JEa-s-IPA2fW_iiS-fOIOZNv6ZZ-ZLpRPxcTAaVk3adtJu9AkpMZZvOhr2w0IqPuIHg"
}

auth0_params = {

    "AUTH0_DOMAIN": "dev-fkoly682.us.auth0.com",
    "ALGORITHMS": "['RS256']",
    "API_AUDIENCE": "discography"


}