# Excluding the original upper ordinary-coordinate face

Research deduction, 6 November 2026. The original face
\(\Re s=.5\) is impossible in the first-four/next-three factorial
height problem. The proof keeps the correlation imposed by the
original \(s\) derivative: it does not maximize the two source
factors independently in their real angles. The final signs are
exact univariate polynomial identities.

## 1. Scope and the correlated angle bound

Use the original phase, unchanged actual heights, outgoing affine
subtraction, and whole factorial path of the
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md).
The word has \(m\ge3\), and the next vertex is an ordinary
type-three vertex. The same bounds as in the
[lower-face exclusion](research_mixed_factorial_lower_face_exclusion.md)
apply:
\[
 \begin{gathered}
 .3<\Re e<.4,\quad -.051<\Im e<-.019,\quad
 .2<\Re s\le.5,\quad .22\le\Re z<3/8,\quad
 .22\le\Re b\le.45,\\
 -.065<\Im s,\Im b<.068,\qquad
 -.07<c\le k=\Im z\le.014 .
 \end{gathered}
 \tag{1}
\]
At a hypothetical maximizer with \(\Re s=.5\), the original
one-sided derivative conditions require
\[
                 D_s:=\Re\mathcal F_s\ge0,\qquad
                 D_z:=\Re\mathcal F_z\le0 .
 \tag{2}
\]
The affine term depends only on \(\Re b\), and the factorial
term \(-2\pi k\) is constant under these real variations.

Write
\[
 S=e^{-2\pi is}=-r,\quad Z=e^{-2\pi iz},\quad
 B=e^{-2\pi ib},\quad E=e^{-2\pi ie},\quad
 R=|Z|,\quad u=\cos(2\pi\Re z).
 \tag{3}
\]
Set the fixed rational constants
\[
 r_0=\frac{13}{20},\quad r_1=\frac{307}{200},\quad
 R_0=\frac{16}{25},\quad g=\frac{47}{250},\quad
 \alpha=\frac{29}{40},\quad
 \lambda=\frac45,\quad \nu=\frac{343}{600}.
 \tag{4}
\]
The elementary witnesses in the lower-face proof give
\(r_0<r<r_1\), \(|B|<r_1\), \(R>R_0\), and
\(|E|>\alpha\). Moreover
\[
 \gamma:=\cos(.44\pi)=\sin(.06\pi)<g,\qquad
                          u\le\gamma<g .
 \tag{5}
\]
For an explicit upper sine witness, use
\(.06\pi<33/175\) and
\[
 g-\left(\frac{33}{175}
      -\frac{(33/175)^3}{6}+\frac{(33/175)^5}{120}\right)
                         =\frac{3572529869}{6565234375000}>0 .
 \tag{6}
\]

Define
\[
 L(r)=1+r_1^2r^2+2gr_1r,\qquad W(r)=(1+r)^4 .
 \tag{7}
\]
Since \(S=-r\) and \(\Re b\in[.22,.45]\),
\[
 |1-SB|^2=1+r^2|B|^2+2r|B|\cos(2\pi\Re b)<L(r).
 \tag{8}
\]
The original chirped derivative is
\[
 e^{2D_s}=\frac{|1-SZ|^2|1-SB|^2}{R^2(1+r)^4}.
 \tag{9}
\]
Thus \(D_s\ge0\) forces the correlated lower bound
\[
 u>u_0(r,R):=
 \frac{R^2W(r)/L(r)-1-r^2R^2}{2rR}.
 \tag{10}
\]
In particular the first real coordinate cannot be varied
independently of this necessary condition.

## 2. The required cosine is strictly positive

Put
\[
 J(r)=(1+r)^3-rL(r).
 \tag{11}
\]
It is positive throughout \(r\in[r_0,r_1]\). In fact,
\[
 J(r)=1+2r+
       \{3-2gr_1+(1-r_1^2)r\}r^2,
 \qquad
 3-2gr_1+(1-r_1^2)r\ge\frac{2728277}{8000000}>0 .
 \tag{12}
\]
The minimum coefficient is at \(r=r_1\).
Consequently
\(W-r^2L=rL+(1+r)J>0\).
The numerator of (10), after multiplication by \(L\), increases
with \(R^2\). Its value at \(R=R_0\) is the polynomial
\[
                  P_0(r)=R_0^2\{W(r)-r^2L(r)\}-L(r)>0 .
 \tag{13}
\]
An exact coefficient proof of the last inequality is given in
Section 5. Therefore (10) implies
\[
                         0<u_0(r,R)<u\le\gamma<g .
 \tag{14}
\]
In particular a point satisfying the required \(s\) sign must
have \(\Re z<.25\).

## 3. A correlated lower bound for the \(z\) derivative

Under (14), the actual private coordinate satisfies
\(.52<\Re(e+z)<.65\). The cosine is increasing on this
summed-real-part interval. Using \(\Re e<.4\),
\[
 \begin{split}
 -\cos(2\pi\Re(e+z))
 &>-\cos(.8\pi+2\pi\Re z)\\
 &=\cos(\pi/5)u+\sin(\pi/5)\sqrt{1-u^2}
                         >\lambda u+\nu .
 \end{split}
 \tag{15}
\]
Here \(\cos(\pi/5)>4/5\) and \(\sin(\pi/5)>7/12\)
are the elementary exact bounds used in the
[cap-curvature proof](research_mixed_private_cap_curvature_bound.md).
Also \(\sqrt{1-u^2}>\sqrt{1-g^2}>49/50\), because
\[
                         1-g^2-(49/50)^2=133/31250>0 .
 \tag{16}
\]
All quantities in the lower bound (15) are positive.

Set
\[
 v=\frac{R^2J(r)}{L(r)},\qquad
 T=\frac{R^2W(r)}{L(r)}=(1+r)(rR^2+v),
 \tag{17}
\]
and define
\[
 \begin{split}
 C(r,R)
 &=1-\frac{\alpha\lambda}{r}
        +\alpha(\alpha+\lambda)R^2+2\alpha\nu R
        +\alpha\lambda(1+1/r)v,\\
 D(r,R)&=\frac{1+r}{r}(1-v).
 \end{split}
 \tag{18}
\]
These are obtained by substituting \(u_0\) into
\(1+\alpha^2R^2+2\alpha R(\lambda u+\nu)\) and
\(1+R^2-2Ru\), respectively. Equations (10), (14)--(15)
then give
\[
 |1-EZ|^2>C(r,R),\qquad
 |1-SZ|^2>T,\qquad
                         0<|1-Z|^2<D(r,R).
 \tag{19}
\]
In particular \(D>0\) under the hypothetical maximizing
conditions. No division by a potentially nonpositive bound
is made. Also \(C>0\), since \(r>\alpha\lambda=29/50\)
and every other term in its displayed formula is positive.

By the original \(z\) derivative, the required sign \(D_z\le0\)
is incompatible with
\[
 \frac{C(r,R)T}{r^2}>D(r,R)^3 .
 \tag{20}
\]
This is exactly the sign of
\[
 \mathcal G(r,R):=
 C(r,R)\,r(rR^2+v)-(1+r)^2(1-v)^3,
 \tag{21}
\]
because the difference in (20) equals
\((1+r)\mathcal G(r,R)/r^3\).

For fixed \(r\), this last expression \(\mathcal G\) is strictly
increasing in \(R>0\). Indeed \(J,L>0\), so \(v=R^2J/L\)
increases; \(C\) is positive and increases; and
\(rR^2+v\) is positive and increases. The derivative of
\(-(1+r)^2(1-v)^3\) is
\(3(1+r)^2(1-v)^2v'\ge0\), even without assuming \(v<1\).
It therefore suffices to prove
\[
                           \mathcal G(r,R_0)>0 .
 \tag{22}
\]
Section 5 supplies an exact positive coefficient identity.
Together (19)--(22) force \(D_z>0\), contradicting (2).

**Theorem.** On the entire original next-three factorial path,
\[
                              \Re s<.5 .
 \tag{23}
\]
The proof did not impose an outgoing stationarity equation or
replace the original external data by a new reference.

## 4. Consequence for the response problem

Combine (23), the proved lower \(s\) exclusion, the
[lower \(z\)-face exclusion](research_mixed_factorial_lower_face_exclusion.md),
and the earlier private-coordinate bounds. The coordinates
\(e_R,s_R,z_R\) are now interior at every factorial maximizer
throughout the reset. Only \(b_R\) may remain on an original
endpoint. Thus both original equations \(D_s=D_z=0\) are available,
and only the first row/first column case of the
[active-face response table](research_mixed_active_face_curvature_budget.md)
remains, with its two choices of outgoing stiffness.

This removes active \(s,z\) cases from that application; it does
not bound the remaining scalar curvature or its weighted integral.
The canonical endpoint constraint, the actual outgoing tangent
and the feasible reference data remain essential. Finite-source
currents and their selected normalization are separate obligations.

## 5. Exact one-variable coefficient identities

Let
\[
 B_i^n(t)=\binom ni t^i(1-t)^{n-i},\quad
 r(t)=\frac{13}{20}+\frac{177}{200}t,\quad 0\le t\le1 .
 \tag{24}
\]
The exact degree-four identity proving (13) is
\[
 \begin{gathered}
 P_0(r(t))=\frac1{1250000000000000}
                              \sum_{i=0}^4p_iB_i^4(t),\\
 (p_0,\ldots,p_4)=
 (318802403475000,\ 824178618411750,\ 1495573816595025,\
                  2323818844354665,\ 2873778691476438).
 \end{gathered}
 \tag{25}
\]
All five coefficients are positive.

For (22), the denominators and the removable positive factor
can be cleared exactly. Define the polynomial
\[
               H(r)=\frac{L(r)^3}{(1+r)^2}\,
                                      \mathcal G(r,R_0).
 \tag{26}
\]
For an explicitly polynomial form, put
\[
 K(r)=r-\alpha\lambda+r\alpha(\alpha+\lambda)R_0^2
                                      +2\alpha\nu rR_0.
\]
Then substitution gives
\[
 H=R_0^2(1+r)L^2K
       +\alpha\lambda R_0^4(1+r)^2LJ-(L-R_0^2J)^3 .
\]
It has degree nine, and
\[
 H(r(t))=\frac1d\sum_{i=0}^9h_iB_i^9(t),\qquad
              d=437500000000000000000000000000000000000000,
 \tag{27}
\]
with the following exact positive numerator vector:
\[
 \begin{pmatrix}h_0\\h_1\\h_2\\h_3\\h_4\\h_5\\h_6\\h_7\\h_8\\h_9\end{pmatrix}
 =
 \begin{pmatrix}
 1303208785098200100439122918057562500000000\\
 1975814254887952717488972432899790000000000\\
 2923048911089081110091559798867566793750000\\
 4215386823048246669203565594198197745750000\\
 5893435531544031377953853885726792349825000\\
 7897874655392216815069758429115385431950000\\
 9921805085682577821960375473295155098288125\\
 11121641030579937790501176897591172292821875\\
 9581235869190978676468666421949763752568380\\
 1357514336245495260373973988367578591323268
 \end{pmatrix}.
 \tag{28}
\]
The defining formulas (7), (11), (17)--(18), (21) and (26)
are rational polynomial expressions, so these coefficient
identities can be checked by expansion alone. For a degree-\(n\)
polynomial \(\sum_j a_jt^j\), its \(i\)-th Bernstein coefficient
is \(\sum_{j=0}^ia_j\binom ij/\binom nj\).
The nonnegative Bernstein weights sum to one. Thus (25) and
(27)--(28) prove strict positivity on the whole closed interval,
without sampling or introducing any new source-root witness.
