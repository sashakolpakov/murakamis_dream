# A necessary height for the original symmetric 343 closing saddle

Private phase deduction, 9 November 2026. The positive geometric
middle angle of the complete-ended symmetric word 343 lies below
the entire height-one-half phase rectangle used for the recent
inner-three estimates. The proof uses the original unsquared
returns, not a numerical root or a root selected from an elimination
polynomial. No finite-source estimate is asserted here.

## 1. Original geometric point and statement

Keep the unique positive unit-charge solution of the complete-ended
path 343 from the
[positive charge theorem](research_positive_path_fractional_charge_cube.md).
Reversal uniqueness identifies its two end angles. Write
\[
 t_g=a-iH,\qquad u_g=\beta-iK,\qquad
 c=\cos(t_g/2)=p+iq,\qquad C=\cos(u_g/2).
\tag{1}
\]
That theorem gives
\[
 0<a,\beta<\pi,\qquad 0<H,K<23/20.
\tag{2}
\]
In particular \(p,q,\Re C,\Im C\) are all strictly positive.
The original logarithmic equations, with both complete outside
incidences retained, are
\[
\begin{split}
 \operatorname{arsinh}\tan(t_g/2)
 +\operatorname{arsinh}\{C\tan(t_g/2)\}
       &=i(3t_g/2-\pi),\\
 \operatorname{arsinh}\{c\tan(u_g/2)\}
       &=i(u_g-\pi/2).
\end{split}
\tag{3}
\]
Every return is the original positive return. The
[exact closing and domain theorem](research_mixed_symmetric_343_closing_trace_and_domain.md),
Section 4, identifies this system with the original symmetric
geometric reference and its calibrated action.

**Proposition.** This actual middle height satisfies
\[
 \boxed{\qquad \cosh K>\frac76,\qquad
       K>\operatorname{arcosh}(7/6)>\frac{17}{30}>\frac12.
       \qquad}
\tag{4}
\]
Consequently its angle cannot belong to any strip
\(|\Im u|\le1/2\), irrespective of its real part. This is
stronger than exclusion from the particular lower rectangle of
the closing and domain theorem. It does not preclude continuation
of the phase or the complete quantum source to a larger domain.

## 2. Two necessary inequalities from the end equation

The unsquared
[Chebyshev elimination](research_two_edge_stationary_chebyshev_trace.md)
applies to the first line of (3) and gives
\[
       4c^3-3c-i(4c^2-1)=C.
\tag{5}
\]
Here the calibrated sign
\(\cosh(\operatorname{arsinh}\tan(t_g/2))=\sec(t_g/2)\)
is retained. Both sides have positive real part and the same
square on the angle domain (2); the sine and cosine divisors
are nonzero there. Thus (5) is a consequence of the actual
logarithmic solution, without a converse assertion about its
other polynomial roots.

The real part of (5) reads
\[
 \Re C=p\{4p^2-12q^2+8q-3\}.
\tag{6}
\]
Since \(p,\Re C>0\),
\[
       p^2>3(q-1/3)^2+5/12
             =3q^2-2q+3/4\ge5/12.
\tag{7}
\]
In particular \(p^2>5/12\), including at \(q=1/3\).

We claim in addition that
\[
                              q>1/4.
\tag{8}
\]
If \(0<q\le1/4\), the coefficient \(12q-4\) is negative.
Use (7) in the imaginary part of (5):
\[
\begin{split}
 \Im C
  &=(12q-4)p^2-4q^3+4q^2-3q+1\\
  &<(12q-4)(3q^2-2q+3/4)-4q^3+4q^2-3q+1\\
  &=2(4q-1)(4q^2-3q+1)\le0.
\end{split}
\tag{9}
\]
The last quadratic is positive:
\(4q^2-3q+1=4(q-3/8)^2+7/16\).
Equation (9) contradicts \(\Im C>0\), proving (8).

## 3. The exact middle return forces the height

Taking the hyperbolic sine of the second line of (3), without
altering its already specified logarithmic lift, gives
\[
                    c\tan(u_g/2)=-i\cos u_g.
\tag{10}
\]
Set \(L=\cosh K\), \(B=\cos\beta\), and
\(S_K=\sinh K\). Since \(L>1\), all the following real
denominators are positive. Substituting
\[
 \tan(u_g/2)=\frac{\sin\beta-iS_K}{B+L},\qquad
 \cos u_g=BL+i\sin\beta\,S_K
\]
into (10), and multiplying by the conjugate of its denominator,
yields the two exact identities
\[
 \boxed{\quad
 p=S_K\left(B+\frac1{L-B}\right),\qquad
 q=\sin\beta\left(L-\frac1{L-B}\right).
 \quad}
\tag{11}
\]
In deriving them one uses
\(\sin^2\beta+S_K^2=(L-B)(L+B)\).

By (8), \(0<\sin\beta\le1\), and the second identity,
\[
 L-\frac1{L-B}>\frac14,
 \qquad
 B<L-\frac1{L-1/4}.
\tag{12}
\]
For fixed \(L\), the first expression in (11) increases
strictly with \(B\), since its derivative is
\(S_K\{1+(L-B)^{-2}\}\). Hence
\[
 p<S_K\left(2L-\frac14-\frac1{L-1/4}\right).
\tag{13}
\]
The expression in parentheses is strictly increasing for
\(L>1\). If \(L\le7/6\), it is at most
\[
       \frac73-\frac14-\frac{12}{11}
                     =\frac{131}{132}<1.
\]
Equations (13) and \(S_K^2=L^2-1\) would therefore imply
\[
                    p<\frac{\sqrt{13}}6
                       <\frac{\sqrt{15}}6=\sqrt{5/12},
\tag{14}
\]
contradicting (7). Thus \(\cosh K>7/6\).

To record a rational height consequence, put \(x=17/30\).
In the positive series for \(\cosh x\), the ratio after its
quadratic term is at most \(x^2/12=289/10800\). Therefore
\[
 \cosh(17/30)
 \le1+\frac{289/1800}{1-289/10800}
 =\frac{12245}{10511}<\frac76,
\tag{15}
\]
where the final comparison is \(73470<73577\).
Monotonicity of \(\cosh\) on the positive axis proves the
rest of (4). This completes the proof.

The deduction only localizes a necessary domain of the actual
positive closing saddle. It does not prove a full inner-three
packet at that saddle, identify a contributing finite contour,
or bound the closing aliases, endpoint currents, or complementary
source. Those remain the distinct source requirements in the
exact closing theorem.

## Source versions

- Original positive charge solution:
  d3806cebb427d94b795e85c5c089592c4646b49ffc01238673f4f9d04f7f3bac.
- Exact symmetric closing and geometric sheet:
  ef74516ae0cc9a4d965f6a528e8f582cfbca43a06e53d017201f3c30b982955a.
- Original unsquared Chebyshev elimination:
  2f4ce35d1729af574c8d482f63ee3a6304c9573f400c146fe2296ce7030be4d3.
