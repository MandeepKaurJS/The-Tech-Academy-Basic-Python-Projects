 }
        [TestMethod]
        public void ReadDocument_Shouldreturn_TwolinewheninputisTwo()
        {
            //arrange
            string expected = "World!";
            //Act
            var result = Helper.ReadDocument(@"C:\AutomateQuizInput\AutomateQuizInput\Docs\TextFile.txt").ToList();
            //assert
            Assert.AreEqual(expected, result[1]);
        }
        [TestMethod]
        public void InputQuizTask_ShouldRetrunQuizzes()
        {
            //arrange
            Quiz quiz = new Quiz();
            quiz.QuizId = 4545;

            string str = $"working on quize {quiz.QuizId}";

            //act
            var x = quiz.InputQuizTask(quiz);
            //Assert.AreSame();
            Assert.AreEqual(str, x);
        }

driver.FindElement(By.Name("course_id")).Click();
new SelectElement(driver.FindElement(By.Name("course_id"))).SelectByText("W2006UPC5WaterHeaterOR_SC");
driver.FindElement(By.XPath("(.//*[normalize-space(text()) and normalize-space(.)='Choose a Course ID'])[1]/following::option[15]")).Click();
driver.FindElement(By.XPath("(.//*[normalize-space(text()) and normalize-space(.)='Choose a Course ID'])[1]/following::input[1]")).Click();
//driver.FindElement(By.XPath("//input[@value='Add Quiz']")).Click();
driver.FindElement(By.Name("course_id")).Click();
driver.FindElement(By.Name("quiz_id")).Click();
driver.FindElement(By.Name("quiz_status")).Click();
driver.FindElement(By.Name("course_page")).Click();
driver.FindElement(By.Name("course_pass_page")).Click();
driver.FindElement(By.XPath("//td/table[2]")).Click();
driver.FindElement(By.Name("course_fail_page")).Click();
driver.FindElement(By.Name("quiz_image_path")).Click();
driver.FindElement(By.Name("quiz_image_path")).Click();
driver.FindElement(By.Name("quiz_comment")).Click();
driver.FindElement(By.Name("button_action")).Click();