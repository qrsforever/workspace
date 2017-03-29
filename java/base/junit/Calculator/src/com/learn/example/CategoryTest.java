package com.learn.example;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.experimental.categories.Categories;
import org.junit.experimental.categories.Categories.ExcludeCategory;
import org.junit.experimental.categories.Categories.IncludeCategory;
import org.junit.runner.RunWith;
import org.junit.runners.Suite.SuiteClasses;

@RunWith(Categories.class)
@IncludeCategory(FastTests.class)
@ExcludeCategory(SlowTests.class)
@SuiteClasses({BlockJUnit4Test.class, RuleTest.class})
public class CategoryTest extends BaseTest { 
    @BeforeClass
    public static void beforeClass() {
        Logger.d("");
    }
    @AfterClass
    public static void AfterClass() {
        Logger.d("");
    }
}
