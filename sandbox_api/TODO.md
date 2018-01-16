## TODO:

### Overall:
* Use Sphinx for docs, theme by Read the Docs
* Create non-root admin account on server -- Stop using root
* Add badges to repo?
* Add ansible
* Add CI -- Heroku, AWS or Jenkins
* Change defualt branch to QA

### Sandbox:
* Overall:
  * Dockerize app
  * Add tox

* Code:
  * Decide on using SQLAlchemy for Loan or if its a normal class
	  * Change LoanController to use Loan model
  * Think about changing controller and view names to make them straight forward
  * Make Loan.amort_sched() a pandas table
  * Serialize amortization tables better (probably fixed with pandas)
  
  * Build out unittests
    * Figure out why tests inside MinProd don't work
    * Code ceverage analysis
  * Build out:
    * Loan Calc
      * Solve issue with slight incorrect answers -- rounding error?
      * Find equations for other functions -- Replace brute force
    * Mortgage Calc
      * Inherit/composed from Loan
    * Car Loan Calc
      * Inherit/composed from Loan
