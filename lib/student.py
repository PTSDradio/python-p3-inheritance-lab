#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    def learn(self, facts):
        self.knowledge.append(facts)
        pass