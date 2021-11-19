Feature: Calculate retirement age
	As an employed worker,
	I want to find my retirement age and date
	So that I know when I will receive social security benefits

	Background:
	Given full_retirement_age.py is run by the user.

Scenario Outline: User looks for retirement age and retirement date
	Given year_of_birth is entered as "<year_of_birth>"
	And month_of_birth is entered as "<month_of_birth>"
	Then the program displays 'Your full retirement age is "<retirement_age>" and "<retirement_month>" months.'
	And the program displays "<future_month>" of "<future_year>"

	Examples: Inputs
	| year_of_birth | month_of_birth| retirement_age| retirement_month	|future_year	| future_month |
#	| 1899	        | 1		        | An error	    |	An error	    | An error      |		An error            |
	| 1900		    | 4		        | 65		    |	0		        | Apr-1965	               |	 4            |
	| 1937		    | 7		        | 65		    |	0		        | Jul-2002	    |	              7          |
	| 1938		    | 12	        | 65		    |	2		        | Feb-2004	    |	               2         |
	| 1942		    | 1		        | 65		    |	10		        | Nov-2007	    |	                11       |
	| 1943		    | 2		        | 66		    |	0		        | Feb-2009	    |	                  2      |
	| 1954		    | 11	        | 66		    |	0		        | Nov-2020	    |	               11         |
	| 1955		    | 9		        | 66		    |	2		        | Nov-2021	    |	               11         |
	| 1956		    | 8		        | 66		    |	4		        | Dec-2022	    |	               12         |
	| 1960		    | 6		        | 67		    |	0		        | Jun-2027	    |	               6         |
	| 1961		    | 10	        | 67		    |	0		        | Oct-2028	    |	               10         |
	| 2000		    | 3		        | 67		    |	0		        | Mar-2067	    |	               3         |
#	| "a"		    | An error	    | An error	    |	An error	    | An error	    |	   An error             |
#	| 2000		    | "a"		    | An error	    |	An error	    | An error	    |	   An error                |
#	| ""		    | Program exit	| Program exit	|	Program exit	| Program exit	|	    An error             |
#	| 2000		    | ""		    | An error	    |	An error	    | An error	    |	     An error               |
#	| 2020		    | An error	    | An error	    |	An error	    | An error	    |	An error |