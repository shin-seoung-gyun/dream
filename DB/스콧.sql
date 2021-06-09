--지역이 NEW YORK인 사원의 사원번호, 사원이름을 사원번호 순으로 검색하라.
select empno, ename from emp join dept using(deptno)where dept.loc='NEW YORK' order by empno;

--ALLEN 사원이 근무 중인 부서이름과 지역을 검색하라(equi join)
SELECT DNAME, LOC FROM EMP,DEPT WHERE emp.deptno=dept.deptno AND ENAME='ALLEN';

--ALLEN 사원이 근무 중인 부서이름과 지역을 검색하라(join ~ using)
SELECT DNAME, LOC FROM EMP JOIN DEPT USING(DEPTNO) WHERE ENAME='ALLEN';

--ALLEN 사원이 근무 중인 부서이름과 지역을 검색하라(join ~ on)
SELECT DNAME, LOC FROM EMP JOIN DEPT ON DEPT.DEPTNO=EMP.DEPTNO WHERE ENAME='ALLEN';

--ALLEN 사원이 근무 중인 부서이름과 지역을 검색하라(natural join)
SELECT DNAME, LOC FROM EMP NATURAL JOIN DEPT WHERE ENAME='ALLEN';

--급여가 2000 이상인 사원들의 사원명과 지역을 검색하라
SELECT ENAME, LOC FROM DEPT, EMP WHERE DEPT.DEPTNO=emp.deptno AND SAL>= 2000;

--급여가 1000 이상 2000 이하인 사원들의 사원번호, 사원이름, 부서이름을 사원번호순으로 검색하라.
SELECT ENAME, LOC FROM DEPT, EMP WHERE DEPT.DEPTNO=emp.deptno AND SAL<= 2000 AND SAL>=1000 ORDER BY EMPNO;

--사원직무가 SALESMAN이면서 CHICAGO 지역에 근무중인 사원명을 검색하라.
SELECT ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='CHICAGO' AND JOB='SALESMAN';

--NEW YORK 이나 DALLAS 지역에 근무하는 사원들의 사원번호와 사원이름을 사원번호 순으로 검색하라(equi join).
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='NEW YORK' OR LOC='DALLAS' ORDER BY EMPNO;

--부서이름이 ACCOUNTING이거나, 지역이 CHICAGO이니 사원의 사원번호와 사원이름을 검색하라.
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC='CHICAGO' OR DNAME='ACCOUNTING';

--NEW YORK이나 DALLAS 지역에 근무하는 사원들의 사원번호와 사원이름을 사원번호 순으로 검색하라(natural join)
SELECT EMPNO, ENAME FROM EMP NATURAL JOIN DEPT WHERE LOC = 'NEW YORK' OR LOC = 'DALLAS' ORDER BY EMPNO;

--부서이름이 ACCOUNTING이거나, 지역이 CHICAGO인 사원의 사원번호와 사원이름을 검색하라(join~using).
SELECT EMPNO, ENAME FROM EMP JOIN DEPT USING(DEPTNO) WHERE LOC = 'CHICAGO' OR DNAME = 'ACCOUNTING';

--사원번호, 사원이름, 급여, 급여등급을 급여등급별 사원번호 순으로 검색하라.
SELECT EMPNO, ENAME, SAL, GRADE FROM EMP,salgrade WHERE SAL>= LOSAL AND SAL <=HISAL ORDER BY GRADE, EMPNO;

--사원번호, 사원이름, 상급자사원번호, 상급자이름을 검색하라(equi join)
SELECT A.EMPNO, A.ENAME, B.EMPNO, B.ENAME FROM EMP A ,EMP B WHERE A.MGR=B.EMPNO;

--사원번호, 사원이름, 상급자사원번호, 상급자이름을 검색하라(join ~~ on)
SELECT A.EMPNO, A.ENAME, B.EMPNO, B.ENAME FROM EMP A JOIN EMP B ON A.MGR=B.EMPNO;

--BLAKE 사원보다 많은 급여를 받는 사원이름을 검색하라(부질의)
SELECT ENAME FROM EMP WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'BLAKE');

--BLAKE 사원보다 많은 급여를 받는 사원이름을 검색하라(self join)
SELECT A.ENAME FROM EMP A, EMP B WHERE B.ENAME='BLAKE' AND A.SAL>B.SAL;

--FORD 사원과 같은 부서에 근무하는 사원이름을 검색하라.
SELECT ENAME FROM EMP WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';

--FORD 사원과 같은 급여를 받는 사원의 사원번호를 검색하라.
SELECT EMPNO FROM EMP WHERE SAL = (SELECT SAL FROM EMP WHERE ENAME = 'FORD')AND NOT ENAME = 'FORD';











