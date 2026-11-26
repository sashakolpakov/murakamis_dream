# A specified complex-index continuation of the complete boundary coefficient

Research proof, 4 November 2026. The frozen manuscripts are unchanged.

The [complete-boundary coefficient theorem](research_complete_boundary_coefficient_asymptotic.md)
gives a nonzero asymptotic for each physical coefficient \(b_{j,N}\),
uniformly on compact real index intervals. A subsequent contour argument
needs more: a specified holomorphic function of the outer index that
agrees with those coefficients and has a uniform complex asymptotic.
We construct such a function here. Its finite definition retains all
ordinary boundary derivatives and both level parities.

The additional terms in the continuation vanish at the physical indices.
Their smallness off the physical grid is proved, rather than inferred
from those zeros. This is the main point of the argument.

## 1. The fixed finite continuation

Let \(G_N\) be the canonical sine factorial, with \(G_N(l)=S_l\),
\[
 S_l=\prod_{h=1}^l2\sin(\pi h/N),\qquad S_0=1.
\]
Use the original Newton polynomials and their signed complete-color
derivatives
\[
 e_l(w)=\frac{\prod_{h=0}^{l-1}(2\cos((2h+1)\pi/N)-w)}{S_l^2},
 \qquad E_{l,k}=(-1)^k e_l^{(k)}(-2).
 \tag{1}
\]
For a complex outer index \(e\), define the finite sum
\[
 C_{N,k}(e)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}E_{l,k}}{S_lG_N(Ne-l)},
 \qquad
 D_N(e)=\exp\left(\frac{\pi i}{2}
                      [N(e-e^2)-e]\right),
 \tag{2}
\]
and put \(\mathfrak b_{N,k}(e)=(-1)^kD_N(e)^{-1}C_{N,k}(e)\).
No cutoff in (2) depends on \(e\).

**Lemma 1.** The functions in (2) are holomorphic on
\(0<\Re e<1\). At every integer \(0\le j<N\),
\[
             \mathfrak b_{N,k}(j/N)=b_{j,N}^{(k)}(-2).
 \tag{3}
\]
At \(j=0\), (3) means the continuous extension from the strip.

*Proof.* The Gamma product defining \(G_N(z)\) shows that its reciprocal
is holomorphic on \(-N<\Re z<N\). In this strip the only poles of
\(G_N\) are those contributed by \(\Gamma(z+1)\), at
\(-1,-2,\ldots,-N+1\); the other Gamma arguments have positive real
part. Each pole is simple, so \(1/G_N(-h)=0\) for \(1\le h<N\).
For \(0<\Re e<1\), every argument \(Ne-l\) in (2) lies in that
strip. Thus (2) is holomorphic. At \(e=j/N\), the terms with \(l>j\)
vanish exactly, whereas \(G_N(j-l)=S_{j-l}\) for \(l\le j\).
Also \(D_N(j/N)=\delta_j\) in equation (1) of the real-index theorem.
Its exact finite boundary formula now gives (3). \(\square\)

This argument uses the prescribed Gamma interpolation, not arbitrary
interpolation of finitely many values.

## 2. Statement of the complex asymptotic

Retain the phase and coefficient of the real-index theorem:
\[
 \begin{split}
 J(z)&=\int_0^z\Log(2\sin\pi v)\,dv,\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 u_c(e)&=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi i e}}}{2},\\
 A_k(e)&=\frac{\sqrt{2\pi}}{\sqrt{-F_{uu}(e,u_c)}}
 \frac{(\tan(\pi u_c)/(4\pi))^k}
 {(2\sin\pi u_c)^{3/2}(2\sin\pi(e-u_c))^{1/2}}.
 \end{split}
 \tag{4}
\]
All branches are the continued branches fixed in that theorem. Write
\(S(e)=F(e,u_c(e))\), and set
\[
                         I=[1/5,9/20].
 \tag{5}
\]

**Theorem 2.** There is a fixed open complex neighborhood
\(\mathcal U\) of \(I\) on which \(S\) and every \(A_k\) are
holomorphic and \(A_k\ne0\), such that, for every fixed integer
\(k\ge0\),
\[
 C_{N,k}(e)=N^{k-3/2}A_k(e)e^{NS(e)}
                  \{1+O_k(N^{-1})\}
 \tag{6}
\]
uniformly on a possibly smaller neighborhood with compact closure in
\(\mathcal U\). The relative error is holomorphic, and every fixed
\(e\)-derivative satisfies the corresponding bound on a smaller
neighborhood. Multiplication by the explicit factor
\((-1)^kD_N(e)^{-1}\) gives the same statement for
\(\mathfrak b_{N,k}\).

The neighborhood does not depend on \(N\). This theorem does not
claim that it contains a prescribed distant complex critical point
of a whole mixed word.

## 3. The extra terms above a physical endpoint

For \(0\le u\le1\), let
\[
 {\cal V}(u)=2\int_0^u\log(2|\cos\pi t|)\,dt-2J(u).
 \tag{7}
\]
The finite real products satisfy, for every fixed \(k\),
\[
 0\le E_{l,k}\le N^{C_k}e^{N{\cal V}(l/N)},\qquad
 S_l=\exp\{NJ(l/N)+O(\log N)\},
 \tag{8}
\]
uniformly through all physical endpoints. These estimates, including
the odd zero and its ordinary derivatives, are proved in Section 3 of
[the complete-boundary calculation](research_mixed_complete_boundary_sum.md).

For real \(e\in I\), the upper exponential bound for the new terms
with \(u\ge e\) is
\[
 H_{\rm ext}(e,u)={\cal V}(u)-J(u)+J(u-e).
 \tag{9}
\]
This is an upper bound obtained by reflection of the reciprocal
factorial. It need not be the rate of a nonzero physical summand,
since those summands vanish when \(e=j/N\).

**Lemma 3.** On \(e\le u\le1/2\), \(H_{\rm ext}(e,u)\) is
strictly decreasing in \(u\). On \(1/2\le u\le1\),
\[
 H_{\rm ext}(e,u)\le1/6,\qquad
 \Re S(e)>12/65>1/6.
 \tag{10}
\]
The inequalities are uniform for \(e\in I\).

*Proof.* On the first interval
\({\cal V}(u)=-2J(1/2-u)-2J(u)\), and hence
\[
 \partial_u H_{\rm ext}
  =\log\frac{\cos^2(\pi u)\sin(\pi(u-e))}{\sin^3(\pi u)}.
 \tag{11}
\]
Put \(z=\tan\pi u\), \(t=\tan\pi e\), \(c=\cos\pi e\),
and \(d=\sin\pi e\). Negativity of (11) is equivalent to
\(z^3-cz+d>0\). For \(z\ge t\), this polynomial is increasing,
because
\[
 3t^2-c\ge
 3\tan^2(\pi/5)-\cos(\pi/5)
             =\frac{59-25\sqrt5}{4}>0.
 \tag{12}
\]
At \(z=t\) its value is \(t^3>0\). This proves the first claim;
continuity includes the endpoints.

The symmetry \({\cal V}(1-u)=-{\cal V}(u)\), and the sign of
\(J\) on either side of \(1/2\), imply
\({\cal V}(u)\le0\) and \(J(u)\ge0\) on the second interval.
Thus \(H_{\rm ext}\le\max_{[0,1]}J\). This maximum is
\(-J(1/6)\), since \(J'(u)=\log(2\sin\pi u)\) and
\(J(1-u)=-J(u)\). Concavity of sine gives
\(\sin\pi t\ge3t\) for \(0\le t\le1/6\); therefore
\[
             -J(1/6)\le-\int_0^{1/6}\log(6t)\,dt=1/6.
 \tag{13}
\]

For the lower bound on the critical action, the endpoint comparison
in Section 3 of the real-index theorem gives
\[
 \Re S(e)>F(e,e)_{\rm real}
             =-2J(1/2-e)-3J(e).
 \tag{14}
\]
Here the notation \(F(e,e)_{\rm real}\) denotes the real part of
the continuous endpoint value. On \([1/20,3/10]\), convexity of
\(J\) bounds it above by the larger of its endpoint values.
First,
\[
 J(1/20)\le\frac1{20}\{\log(\pi/10)-1\}<-1/10,
\]
using \(\pi/10<1/3\) and \(\log3>1\). Second,
\[
 -J(3/10)=\int_{3/10}^{1/2}\log(2\sin\pi t)\,dt
 \ge\frac15\log\frac{1+\sqrt5}{2}>\frac6{65}.
 \tag{15}
\]
The last inequality follows from \((1+\sqrt5)/2>8/5\) and
\(\log(1+x)>2x/(2+x)\) for \(x>0\). The latter follows by
differentiating the difference and fixing its value at zero.
Consequently \(-2J(1/2-e)>12/65\). Since \(J(e)<0\) on \(I\),
(14) proves the last inequality in (10). The margin over \(1/6\)
is \(7/390\). \(\square\)

Together with the strict real endpoint gap of the real-index theorem,
Lemma 3 places every added high-index term below the critical rate.
The comparison includes \(u=1/2\), both level parities, and all fixed
ordinary boundary derivatives.

## 4. Uniform bounds off the physical grid

We specify the bound used to move off the real \(e\)-interval. Let
\(v=e-u\). Away from the negative real axis, continue \(J\) from
the upper or lower side, denoting these branches by \(J_+(v)\)
and \(J_-(v)\). For negative real \(v\), their real boundary values
agree and equal \(-J(-v)\). On a fixed rectangle avoiding the
endpoints \(v=\pm1\), the reflected factorial bounds give
\[
 |G_N(Nv)^{-1}|
       \le N^C e^{-N\Re J_{\rm side}(v)}.
 \tag{16}
\]
This includes the negative-integer zeros of the reciprocal. To obtain
(16) directly from Section 2 of
[the uniform factorial bounds](research_uniform_factorial_and_boundary_decay.md),
write \(Nv=N(v+1/(2N))-1/2\). The midpoint bound applies on
both sides of zero. Changing the primitive argument by \(1/(2N)\)
costs \(O(\log N/N)\) uniformly, because its only intervening
singularity is logarithmic. Where that short shift crosses zero,
use its continuous real upper extension. The same polynomial factor
then proves (16).

On this rectangle the real upper exponent in (16) is uniformly
continuous in \(v\). More precisely, its change under displacement
of size \(h\le1/2\) is at most \(C h(1+|\log h|)\).
Near zero this follows by integrating \(O(1+|\log|v||)\);
away from zero the logarithmic derivative is bounded. The two side
branches have the same real limit on the negative axis, so the
bound also holds across that axis.

Combining (8) and (16), the absolute value of each term of (2),
before its carrier \(D_N^{-1}\), is bounded by a fixed power of
\(N\) times
\[
 \exp N\left\{{\cal V}(u)-J(u)-\Re J_{\rm side}(e-u)
                                      -\pi u\,\Im e\right\}.
 \tag{17}
\]
At real \(e\) this exponent is \(B(e,u)\) for \(u\le e\)
and (9) for \(u\ge e\). The uniform continuity just proved
controls its change on a fixed small complex \(e\)-neighborhood,
including the moving endpoint \(u=\Re e\).

## 5. The entire complex continuation has the selected coefficient

Fix a real \(e_0\in I\). In the real-index proof choose two
fixed cuts strictly inside \((0,e_0)\), enclosing \(u_c(e_0)\)
in real part, with strict gaps on the omitted real intervals and
on the upper vertical sides. These cuts may be kept fixed for
all \(e\) in a small complex disk about \(e_0\).

For the terms outside the cuts, including all \(u>e_0\), the
real gaps follow from the real-index proof and Lemma 3. They
have a uniform positive minimum: the middle upper interval is
controlled by the endpoint gap and monotonicity, and the part
above \(1/2\) has the explicit margin \(7/390\).
Equations (16)--(17), and continuity of \(\Re S(e)\), preserve
half this margin on a sufficiently small complex disk. Summing
the at most \(N\) omitted terms changes only the polynomial
prefactor.

On the retained fixed interval, use the exact holomorphic summand
and its ordinary-jet symbol from Section 2 of the real-index theorem.
All factorial arguments remain in their regular strips. Its
half-grid residue rectangle, both vertical sides, and both Fourier
aliases have strict gaps at \(e_0\). Those gaps persist on a
small complex disk by uniform continuity on the fixed contours.
The saddle continues holomorphically and stays simple. Deforming
the central horizontal segment by a small amount to its continued
saddle is legal inside the same regular compact set; its short
joining segments remain gapped. Gaussian integration therefore
gives exactly the holomorphic continuation of \(A_k(e)\) and
\(S(e)\) in (4), with relative error \(O_k(N^{-1})\).

Crucially, these arguments estimate the single specified finite
function (2). The cuts only split its terms for the proof; they
do not define different interpolants on overlapping disks.
Compactness of \(I\) supplies a finite cover and a common smaller
complex neighborhood. The relative error in (6) is holomorphic,
since its defining denominator is nonzero there. Cauchy's estimate
gives all fixed outer-index derivatives on smaller neighborhoods.
This proves Theorem 2.

## 6. Its finite polynomial and exact difference equation

The fixed continuation also has a finite algebraic expression. Put
\[
 q=e^{\pi i/N},\quad r=q^{-2},\quad P_l=(r;r)_l,\quad
 (Y;r)_l=\prod_{h=0}^{l-1}(1-Yr^h),\quad Y=e^{2\pi i e}.
\]
The factorial recurrence in (2) gives, for every fixed \(k\),
\[
 \begin{split}
 G_N(Ne)C_{N,k}(e)&=H_{N,k}(Y),\\
 H_{N,k}(Y)&=\sum_{l=0}^{N-1}
       \frac{(-q)^{-l}E_{l,k}}{P_l}(Y;r)_l .
 \end{split}
 \tag{18}
\]
Indeed
\[
 G_N(Ne)/G_N(Ne-l)
   =\prod_{h=0}^{l-1}2\sin\pi(e-h/N),
\]
and multiplication by \(e^{i\pi e l}/S_l\) changes this product
exactly to \((-q)^{-l}(Y;r)_l/P_l\).
Thus the continuation is a specified degree-at-most-\(N-1\)
polynomial divided by its marked factorial factor.

At ordinary derivative order zero write \(H_N=H_{N,0}\). The
complete Newton product yields
\[
 E_{l,0}=(-q)^{-l}\frac{(-q^{-1};r)_l^2}{P_l^2},\qquad
 H_N(Y)=\sum_{l=0}^{N-1}h_l(Y;r)_l,\qquad
 h_l=\frac{r^l(-q^{-1};r)_l^2}{P_l^3}.
 \tag{19}
\]
In particular \(H_N(1)=1\), fixing its scalar.

Let \(\sigma f(Y)=f(rY)\) and define two operators on polynomials:
\[
 {\cal T}=(1-Y)\sigma,\qquad
 {\cal R}=Y^{-1}(1-{\cal T}).
 \tag{20}
\]
The apparent division by \(Y\) is removable on every polynomial.
Writing \(U_l(Y)=(Y;r)_l\), their exact actions are
\[
                 {\cal T}U_l=U_{l+1},\qquad
                 {\cal R}U_l=r^lU_l.
 \tag{21}
\]
The order of the factors in the following equation is part of
the statement.

**Proposition 4.** The polynomial in (19) satisfies
\[
 \boxed{\quad
 \bigl[(1-{\cal R})^3-r{\cal T}(1+q^{-1}{\cal R})^2\bigr]H_N
   =-\frac{(1+(-1)^N)^2}{N^3}(1-Y^N).
 \quad}
 \tag{22}
\]
It is the unique polynomial of degree at most \(N-1\) satisfying
(22) and \(H_N(1)=1\).

*Proof.* The coefficients in (19) have the exact ratio
\[
 (1-r^{l+1})^3h_{l+1}
         =r(1+q^{-1}r^l)^2h_l,\qquad 0\le l<N-1.
 \tag{23}
\]
Equations (21) and (23) cancel every coefficient of
\(U_1,\ldots,U_{N-1}\) on the left of (22). The last term is
\(-rh_{N-1}(1+q)^2U_N\). Here \(P_{N-1}=N\),
\[
 (-q^{-1};r)_N=1-(-q^{-1})^N=1+(-1)^N,\qquad
 U_N=1-Y^N,
\]
so this last term is exactly the right side of (22).
Conversely, evaluation at \(Y=1\) fixes \(h_0=1\), and the
coefficients of \(U_1,\ldots,U_{N-1}\) force (23), whose
denominators are nonzero. This proves uniqueness. \(\square\)

At odd levels the forcing in (22) vanishes; at even levels it
is \(-4(1-Y^N)/N^3\). It cannot be deleted when defining the
actual polynomial solution.

There is also an exact check of the classical branch selected by
the asymptotic. Replace \(\sigma\) by a commuting variable
\(\Lambda\), and formally put \(q=r=1\). Away from \(Y=0,1\),
the symbol of the operator in (22), after removing its displayed
scalar factor \((1-Y)/Y^3\), is
\[
 {\cal A}(Y,\Lambda)
   =(1-Y)^2(\Lambda-1)^3
       -Y\Lambda\{Y+1-(1-Y)\Lambda\}^2 .
 \tag{24}
\]
The proved asymptotic (6), multiplied by \(G_N(Ne)\) as in
(18), selects
\[
 \Lambda=\exp[-J'(e)-S'(e)]
          =\frac{Y-U}{(Y-1)U},\qquad
                      U=e^{2\pi i u_c(e)}.
 \tag{25}
\]
Substitution into the unremoved symbol gives precisely
\[
 \frac{(1+U)^2(Y-U)-(1-U)^3}{U^3}=0,
 \tag{26}
\]
which is the already proved endpoint stationary equation.
Thus the finite polynomial, its forced difference equation, its
normalization, and its selected asymptotic branch agree exactly.
Equation (24) is the classical polynomial of this boundary
operator; no identification with a knot's \(A\)-polynomial is
asserted.

## 7. Scope and reproduction

This result supplies one explicit complex-index boundary function
with a nonzero full-sum asymptotic and exact agreement with the
original physical coefficients. The neighborhood is fixed as
\(N\to\infty\); no quantitative radius sufficient for every
mixed-word geometric saddle is asserted. The remaining interior
conditional sums and their joint contour still require their own
estimates.

Run the focused checker:

    python3 experiments/check_complete_boundary_complex_index.py

Its exact tests cover the finite-grid truncation, original boundary
normalization and algebraic inequalities. Its finite complex
comparisons are diagnostics. The uniform off-grid gap and the
nonzero coefficient follow from the written proof.
