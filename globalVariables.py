#!/usr/bin/python

message = "How you doing?"

def getGreeting():
  message = "How are you?"
  print("Message inside function -", message)

def getGlobalGreeting():
  global message
  message = "How are you?"
  print("Message inside function -", message)

getGreeting()

print("Message outside function -", message)

getGlobalGreeting()

print("Message outside function -", message)