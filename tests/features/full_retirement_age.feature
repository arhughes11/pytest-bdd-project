Feature: Calculate retirement age
	As an employed worker,
	I want to find my retirement age and date
	So that I know when I will receive social security benefits

	Scenario Outline: User looks for retirement age and retirement date
	Given year_of_birth is entered as <yob>, month_ob_birth is entered as <mob>
	Then the program displays Your full retirement age is <retirement_age> and <retirement_month> months
	And the program displays <future_month> of <future_year>

	Examples: Inputs
	| yob		    | mob			| retirement_age| retirement_month	| future_year | future_month |
	| 1900		    | 4		        | 65		    |	0	            | 1965	      | 4            |
	| 1937		    | 7		        | 65		    |	0	            | 2002        | 7            |
	| 1938		    | 12	        | 65		    |	2	            | 2004        | 2            |
	| 1942		    | 1		        | 65		    |	10	            | 2007        | 11           |
	| 1943		    | 2			    | 66	        |	0	            | 2009        | 2            |
	| 1954		    | 11	        | 66		    |	0		        | 2020        | 11           |
	| 1955		    | 9		        | 66		    |	2		        | 2021        | 11           |
	| 1956		    | 8		        | 66		    |	4		        | 2022        | 12           |
	| 1960		    | 6		        | 67		    |	0		        | 2027        | 6            |
	| 1961		    | 10	        | 67		    |	0		        | 2028        | 10           |
	| 2000		    | 3		        | 67		    |	0		        | 2067        | 3            |
