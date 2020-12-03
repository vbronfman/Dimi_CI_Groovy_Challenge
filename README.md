#  Dimi_CI_Groovy_Challenge

## Overview
Please make a pipeline (preferrably groovy on Jenkins) that is connected to a git server of your choice (gitlab, github, etc.) and reacts on pushes to branches / pull requests / merge requests , could be even triggered from crontab if it is more convenient to implement this way.

- Assume you have branch master in your repo
- Assume you push code to feature branch
- Assume you have a test script for you code (either in groovy or bash or python) that does essentially the following: prints the hash of the current git commit and waits ~3 min. It is expected to always pass but simulates a real test on your commit
- Please make a pipeline that merges the master into the feature branch; fails if merge fails; runs the fake "test" as per description above; checks if while it is running, master has advanced ; if master stayed the same, pushes the feature branch to master ; if master has been changed during the run, runs again (again, merge from master, and again, fake "test")
- If you trigger it on 2 concurrent commits which do not lead to merge conflict, I expect at least one of the two commits to be tested twice (having at least 2 merges from master). Under no circumstances I can expect master branch to be updated with an untested commit
- If you trigger it on 2 concurrent commits which present merge conflict one with the other I expect it to fail on one of the pipelines

I expect groovy (or other, if needed) code for that, and quick demo afterwards. On every stage, don't hesitate to call and ask any questions. 

Thank you! 

Kind regards, 
Dimi

## Usage

```python
import unittest
import re
from app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
      tester = app.test_client(self)
      response = tester.get('/', content_type='html/text')
      self.assertEqual(response.status_code, 200)
      self.assertRegexpMatches(response.data, b'Hello World! I have been seen') #Hello World! I have been seen 5 times.
    def test_other(self):
      tester = app.test_client(self)
      response = tester.get('a', content_type='html/text')
      self.assertEqual(response.status_code, 404)
      self.assertFalse(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()
```
  .\Develop\Dimi_CI_Groovy_Challenge\composetest>docker-compose -f docker-compose.yml exec web python app.test.py
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

Links
http://github.com - automatic!
[GitHub](http://github.com)

https://guides.github.com/features/mastering-markdown/
