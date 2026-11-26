# Exact curvature formulas for adjoining phase terms

Research deduction, 6 November 2026. This note simplifies the effective
curvature in the [boundary-height argument](research_mixed_selected_boundary_height_envelope.md).
It gives exact formulas, including the loss incurred by bounding
adjoining terms separately. It does not prove the proposed bound
of six pi along every maximizing path.

## 1. The quantity to be estimated

Let a holomorphic phase have normalized negative Hessian

\[
 H=-\Phi''/\pi=A+iC,\qquad A\succ0.
 \tag{1}
\]

All entries of the real symmetric matrices \(A,C\) are evaluated
at one fixed complex point. Let \(v\) select the coordinate whose
imaginary part is changing. The dimensionless effective curvature is

\[
 \mathcal K(H;v)=v^TAv+(Cv)^TA^{-1}(Cv).
 \tag{2}
\]

The actual curvature in the height-envelope lemma is
\(\pi\mathcal K\). Formula (2) is exact for an interior
horizontal maximizer and remains an upper bound at a constrained
maximizer. An outgoing affine subtraction changes neither Hessian.

The elementary variational identity

\[
 q^TA^{-1}q=\sup_y\{2q^Ty-y^TAy\},\qquad q=Cv,
 \tag{3}
\]

will also be useful. In particular, adding a positive semidefinite
real matrix that has zero row and column at the changing coordinate,
without changing \(Cv\), cannot increase (2).

## 2. An exact formula for one pair

Use the original primitive \(g\), for which
\(g''(z)=\pi\cot(\pi z)-i\pi\). For \(t\in\{1,-1\}\), put

\[
 \Phi_t(v,w)=g(v+w)-g(v)-g(w)+(1-t)\pi i vw.
 \tag{4}
\]

Thus \(t=1\) gives the unmodified pair, and \(t=-1\) includes
the original chirp \(2\pi i vw\). Write

\[
 p=\cot\pi v=a+ib,\quad q=\cot\pi w=c+id,
 \quad r=\frac{pq-1}{p+q}=r_R+ir_I.
 \tag{5}
\]

Assume

\[
 a\ge0,\qquad c>0,\qquad |b|<1,\quad |d|<1.
 \tag{6}
\]

These hypotheses hold on the smaller horizontal box in Section 12
of the height-envelope note. In particular they allow the face
\(\Re v=1/2\), where \(a=0\).

**Proposition 1.** The real part of

\[
 H_t=-\Phi_t''/\pi
 =\begin{pmatrix}p-r&-r+it\\-r+it&q-r\end{pmatrix}
 \tag{7}
\]

is positive definite. For a change in the imaginary part of \(w\),
its effective curvature is exactly

\[
 \boxed{\displaystyle
 \mathcal K_t=
 \frac{2\{c^2+(d-t)^2\}}
 {a(1-td)+c(1+tb)}.}
 \tag{8}
\]

*Proof.* Put
\(D_+=a(1-d)+c(1+b)\),
\(D_-=a(1+d)+c(1-b)\), and
\(Q=(a+c)^2+(b+d)^2\). Both \(D_+,D_-\) are positive.
The cotangent addition formula gives

\[
 \det\Re H_t=ac-(a+c)r_R=\frac{D_+D_-}{Q}>0.
 \tag{9}
\]

Consequently \(r_R<ac/(a+c)\), so both diagonal entries
\(a-r_R,c-r_R\) are positive, including when \(a=0\).
For the second coordinate, \(Cv=(t-r_I,d-r_I)^T\).
Using the inverse of this two by two real matrix, (2) becomes

\[
 c-r_R+
 \frac{(c-r_R)(t-r_I)^2
       +2r_R(t-r_I)(d-r_I)
       +(a-r_R)(d-r_I)^2}
 {ac-(a+c)r_R}.
 \tag{10}
\]

Substitute

\[
 \begin{split}
 Qr_R&=(ac-bd-1)(a+c)+(ad+bc)(b+d),\\
 Qr_I&=(ad+bc)(a+c)-(ac-bd-1)(b+d).
 \end{split}
 \tag{11}
\]

For \(t=1\) the expression reduces to
\(2\{c^2+(d-1)^2\}/D_+\); for \(t=-1\) it reduces to
\(2\{c^2+(d+1)^2\}/D_-\). This proves (8). Every
denominator used is positive. \(\square\)

There is also a useful exact expression for the response after
eliminating the private real coordinate \(v\). Define

\[
 T=c-r_R-\frac{r_R^2}{a-r_R},\qquad
 U=d-r_I+\frac{r_R(t-r_I)}{a-r_R}.
 \tag{12}
\]

Then \(T>0\), and the same calculation gives

\[
 \frac UT=t\,
 \frac{ac-(1+tb)(1-td)}{a(1-td)+c(1+tb)}.
 \tag{13}
\]

In particular the sign of this response is not fixed by positivity
of the real Hessian. The two choices of chirp can give opposite
responses at a shared coordinate. Taking absolute values of these
responses before combining the terms can lose a useful estimate.

## 3. The canonical endpoint Hessian

Let \(u=u_c(e)\) be the original endpoint critical point and
\(S(e)\) its critical action. Use the exponentials

\[
 U=e^{2\pi i u},\qquad E=e^{-2\pi i e},\qquad
 D(U)=5U^2-2U+1.
 \tag{14}
\]

The [original rational endpoint equations](research_mixed_rational_critical_transport.md)
give \(E=(U+1)^2/D(U)\). Define

\[
 R=\frac{(U+1)(3U-1)}{D(U)}.
 \tag{15}
\]

**Proposition 2.** On the canonical regular endpoint branch,

\[
 \begin{split}
 R^2&=E(2-E),\\
 \sigma:=-S''(e)/\pi
 &=\cot\pi e+\frac{2(\cot\pi e-i)}R\\
 &=\frac{i(19U^3+3U^2+U+1)}{2U(U-1)(3U-1)}.
 \end{split}
 \tag{16}
\]

*Proof.* The first identity follows from
\(2D(U)-(U+1)^2=(3U-1)^2\). To check the second derivative,
use the original endpoint Schur complement from Section 11 of the
height-envelope note:

\[
 \eta=i\frac{U^{-1}+E}{U^{-1}-E},\qquad
 \xi=-2i\frac{1-U^{-1}}{1+U^{-1}}
       +3i\frac{1+U^{-1}}{1-U^{-1}},\qquad
 \sigma=\eta-\frac{(\eta+i)^2}{\xi+\eta}.
 \tag{17}
\]

Substituting \(E=(U+1)^2/D(U)\) in (17) gives the last
expression in (16). Substituting the same expression for \(E\)
and (15) in the middle expression gives that rational function too.
All substitutions are within the original regular branch. In
particular \(U\ne0,1\); the simple canonical endpoint root
has \(E(2-E)\ne0\), so \(U\ne1/3\). \(\square\)

Equation (15), rather than an arbitrary square-root choice, specifies
\(R\). The old expression (17) and the new one (16) are identical;
no new endpoint solution is introduced. Only \(\Re\sigma\)
enters the effective curvature for a change in the attached coordinate
\(z\): the imaginary part of the endpoint's \(ee\) entry
does not belong to the relevant column \(Cv\).

## 4. Joining terms at one shared coordinate

Here is an exact general form of the coupling correction. Suppose
phase terms share one coordinate \(z\), and otherwise have disjoint
private real coordinates. For the \(i\)-th term write its positive
real Hessian and relevant imaginary column in block form:

\[
 A_i=\begin{pmatrix}B_i&b_i\\b_i^T&c_i\end{pmatrix},
 \qquad C_i v=\binom{a_i}{d_i}.
 \tag{18}
\]

All entries in (18) are real, and \(B_i\succ0\). Define

\[
 T_i=c_i-b_i^TB_i^{-1}b_i>0,\quad
 U_i=d_i-b_i^TB_i^{-1}a_i,\quad
 R_i=c_i+a_i^TB_i^{-1}a_i.
 \tag{19}
\]

A term with no private coordinate is allowed: then
\(T_i=R_i=c_i>0\) and \(U_i=d_i\).

**Proposition 3.** The individual and combined curvatures satisfy

\[
 \mathcal K_i=R_i+U_i^2/T_i,
 \qquad
 \mathcal K_{\rm combined}
       =\sum_iR_i+\frac{(\sum_iU_i)^2}{\sum_iT_i}.
 \tag{20}
\]

Consequently

\[
 \boxed{\displaystyle
 \sum_i\mathcal K_i-\mathcal K_{\rm combined}
 =\frac1{\sum_iT_i}
   \sum_{i<j}\frac{(T_jU_i-T_iU_j)^2}{T_iT_j}\ge0.}
 \tag{21}
\]

*Proof.* Eliminate each private block \(B_i\) in the quadratic
form (3). Its independent contribution is
\(a_i^TB_i^{-1}a_i\); the remaining quadratic coefficient at
the shared coordinate is \(T_i\), and its linear coefficient
is \(U_i\). Summing before taking the last supremum gives
(20). Expanding the square proves (21). Equality holds exactly
when every ratio \(U_i/T_i\) is the same. \(\square\)

Thus the weighted Cauchy inequality behind a separate bound has
an explicit nonnegative error. Keeping that error is useful when
the imaginary responses of the adjoining terms differ.

## 5. Application to the first selected boundary coordinate

For the first selected type-four coordinate of a mixed word of length
at least three, with an ordinary next block of type \(3+\epsilon\),
split its four-variable phase into three terms:

\[
 \begin{split}
 \Phi_{\rm cap}(e,z)
   &=S(e)+g(e+z)-g(e)-g(z)-\tfrac{i\pi}{2}(e-e^2),\\
 \Phi_{\rm ord}(s,b,z)
   &=\Phi_{-1}(s,z)+\Phi_1(s,b)
                           -\epsilon g(s)-\tfrac\epsilon2g(b),\\
 \Phi_{\rm diag}(z)&=-g(z).
 \end{split}
 \tag{22}
\]

Their sum is exactly \(\mathcal F\) in the height-envelope note.
Section 12 there proves that all three real Hessians are positive
definite on their own variables in the restricted box. Their private
coordinates are respectively \(e\), \((s,b)\), and none.
Proposition 3 therefore computes the full curvature, including
optimization in the outgoing real variable \(b\), without
separately maximizing its three contributions.

For the last term, with \(\cot\pi z=c+id\),

\[
 T_{\rm diag}=R_{\rm diag}=c,
 \quad U_{\rm diag}=d-1,
 \quad \mathcal K_{\rm diag}=\frac{c^2+(d-1)^2}{c}.
 \tag{23}
\]

There are also simple, weaker upper bounds for the other two terms.
The endpoint action adds the positive entry \(\Re\sigma\)
to the private diagonal of the pair \(\Phi_1(e,z)\), and
does not change its relevant imaginary column. Similarly
\(\Phi_1(s,b)-\epsilon g(s)-\epsilon g(b)/2\) adds a
positive semidefinite real Hessian with zero \(z\) row and column
to \(\Phi_{-1}(s,z)\), without changing that column.
The variational formula (3) therefore gives

\[
 \mathcal K(\mathcal F)
 \le \mathcal K_1(e,z)+\mathcal K_{-1}(s,z)
             +\frac{c^2+(d-1)^2}{c}.
 \tag{24}
\]

For the second comparison the additional variable \(b\) is harmless:
before adding its Hessian the quadratic form in (3) is independent
of \(b\); subtracting a nonnegative form cannot increase its
supremum. Formula (24) discards both this positive contribution and
the exact correction (21), so it need not be sharp enough for the
desired estimate. Formula (20), with (16) retained in the cap, loses
neither contribution.

For the forced phase \(\mathcal F+g(z)\), omit the diagonal
term from (22). The same two-block identity applies. This does not
assert that its maximizing point agrees with the original phase's
maximizer.

These identities apply pointwise, hence also at constrained optimizing
points where the height-envelope lemma uses them as upper bounds.
They preserve the reference heights and original outgoing tangent.
They supply neither a uniform sign for the outstanding curvature
numerator nor estimates for the other finite Fourier terms, contour
ends, or lattice corrections. No new volume identity follows from
this note alone.

## 6. A sufficient real matrix test without the cap square root

At a factorial-branch maximizing point in Section 12 of the
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md),
use the following real quantities from its Section 8. Write
\(p_e=\cot\pi e\), \(p_s=\cot\pi s\),
\(p_z=\cot\pi z\), \(p_b=\cot\pi b\), and put
\(d=\cot\pi(e+z)\), \(f=\cot\pi(s+z)\),
\(j=\cot\pi(s+b)\). Here \(p_b\) denotes this cotangent only;
it is not the outgoing affine marginal. Define
\[
\begin{split}
 B_0&=\Re\{(1+\epsilon/2)p_b-j\}>0,\\
 T_0&=\Re\{(2+\epsilon)p_s-f-j\}
                      -\frac{(\Re j)^2}{B_0}>0,\\
 a_0&=\Re(3p_z-d-f),\qquad
 b_e=-\Re d,\quad b_s=-\Re f,\\
 q_e&=1-\Im d,\qquad q_s=-1-\Im f,
 \qquad q_z=\Im(3p_z-d-f)-1.
\end{split}
\tag{25}
\]
The positivity assertions follow from the already-proved positive
real Hessian. The original normalized private diagonal is
\(E_0=\Re\sigma+\Re p_e+b_e\).
The [stronger private-cap bound](research_mixed_private_cap_curvature_bound.md)
gives
\[
 L\in\left\{\frac{163}{90},\,2\Re p_e+\frac{109}{90}\right\},\qquad
 \overline E=L+b_e>0,\qquad E_0>\overline E.
\tag{26}
\]
Either displayed choice is valid pointwise. The second retains the
private cotangent and is strictly larger, so it gives a less
restrictive sufficient test below. No derivative of \(L\) is taken:
these are comparisons of Hessian matrices at the original point,
not definitions of a replacement phase.
In particular \(b_e>0\), since the optimizing restrictions give
\(1/2<\Re(e+z)<1\). All heights, the canonical endpoint action,
and the outgoing affine subtraction remain the original ones.

**Proposition 4.** A sufficient condition for
\(K_{\rm eff}\le6\pi\) at this point is
\[
 \overline M:=
 \begin{pmatrix}
 T_0&b_s&q_s\\
 b_s&a_0-b_e^2/\overline E&q_z-b_eq_e/\overline E\\
 q_s&q_z-b_eq_e/\overline E&6-a_0-q_e^2/\overline E
 \end{pmatrix}\succeq0.
\tag{27}
\]
Equivalently, define
\[
\begin{split}
 \overline D&=a_0-\frac{b_e^2}{\overline E}
                         -\frac{b_s^2}{T_0},\\
 \overline U&=q_z-\frac{b_eq_e}{\overline E}
                         -\frac{b_sq_s}{T_0},\\
 \overline V&=6-a_0-\frac{q_e^2}{\overline E}
                         -\frac{q_s^2}{T_0}.
\end{split}
\tag{28}
\]
Then (27) holds exactly when
\[
 \overline D\ge0,\qquad \overline V\ge0,
 \qquad \overline D\,\overline V-\overline U^2\ge0.
\tag{29}
\]
There is no assertion here that these last inequalities hold on the
whole optimizing family.

*Proof.* Let \(A=\Re(-\mathcal F''/\pi)\) and let
\(q=\Im(-\mathcal F''/\pi)\mathbf e_z\). Since \(A\succ0\),
the exact curvature formula gives
\[
 K_{\rm eff}/\pi\le6
 \quad\Longleftrightarrow\quad
 \begin{pmatrix}A&q\\q^T&6-a_0\end{pmatrix}\succeq0.
\tag{30}
\]
Here the imaginary column has entries \((q_e,q_s,q_z,0)\)
in the order \((e,s,z,b)\). Lower just the real \(ee\) entry
from \(E_0\) to \(\overline E\), keeping every other entry
of (30) unchanged. If the resulting matrix is positive
semidefinite, adding back the positive \(ee\) surplus proves
(30). Eliminate its \(b\) coordinate using \(B_0>0\), and
then its \(e\) coordinate using \(\overline E>0\).
The remaining matrix in the order \((s,z,\text{last})\) is
exactly (27). Eliminating \(s\) using \(T_0>0\) leaves the
two by two matrix with entries
\(\overline D,\overline U,\overline V\); its positive
semidefiniteness is precisely (29). \(\square\)

In this particular optimizing domain, the first inequality in (29)
has a separate strict proof. The lowered real cap Hessian is the
positive pair Hessian for \(\Phi_1(e,z)\), plus the private
diagonal
\[
              L-\Re p_e>\frac{163}{90}-\frac34
                                      =\frac{191}{180}>0.
\tag{31}
\]
This uses the cotangent rectangle proved in the stronger cap note.
The ordinary block and the extra \(-g(z)\) retain their positive
real Hessians from (22). Thus the entire lowered real Hessian is
positive definite; no positivity is being inferred merely from
lowering a diagonal. More explicitly, if \(c=\Re p_z>0\),
its cap contribution after private elimination is
\[
 c+b_e-\frac{b_e^2}{L+b_e}
            =c+\frac{Lb_e}{L+b_e}>c.
\tag{32}
\]
The ordinary block contributes a strictly positive Schur complement,
and \(-g(z)\) contributes \(c\). Consequently
\(\overline D>2c>0\). In this domain the final determinant
inequality in (29) would therefore also imply
\(\overline V\ge0\).

The test removes \(\sigma\) and its canonical square root from a
sufficient curvature comparison, without changing the original
phase or its maximizing points. It is weaker than the exact test
with \(E_0\): failure of (29) would not refute the desired curvature
bound. The determinant sign is still unproved. The original
stationary modulus equations, the actual reference relation and
outgoing marginal, and the next-external compatibility must still
be retained when attempting it; neither an independent rectangular
replacement of these correlations nor a general product-height
inequality has been established.

## 7. The exact effect of extra private curvature

The pair formula also measures exactly how a positive private
curvature changes the response. Use the notation of Proposition 1,
and write \(\mathcal K_+,\mathcal K_-\) for (8) at the same
pair of complex coordinates, with its two possible chirps.
Let \(A=\Re H_t\), which is independent of \(t\), and
\(q_t=(t-r_I,d-r_I)^T\). For \(s_0>0\), replace
\(A\) by \(A+s_0\mathbf e_1\mathbf e_1^T\), keeping
the relevant imaginary column \(q_t\) unchanged. Let
\(\mathcal K_t(s_0)\) denote its resulting curvature.

**Proposition 5.** The exact formula is

\[
 \mathcal K_t(s_0)
  =\mathcal K_t-
       \frac{s_0\mathcal K_t^2}{4+s_0(\mathcal K_++\mathcal K_-)}
  =\left(\frac1{\mathcal K_t}
         +\frac1{\mathcal K_{-t}+4/s_0}\right)^{-1}.
 \tag{33}
\]

*Proof.* Put \(n_\pm=c^2+(d\mp1)^2\), and use
\(D_\pm,Q\) from the proof of Proposition 1. Expanding gives

\[
 2Q(c-r_R)=n_+D_-+n_-D_+,
 \qquad (A^{-1})_{11}=\frac{\mathcal K_++\mathcal K_-}{4}.
 \tag{34}
\]

The second identity follows from (9) and the first. Write
\(q_t=q_0+t\mathbf e_1\). Subtracting the two curvature
formulas gives
\(\mathcal K_+-\mathcal K_-=4\mathbf e_1^TA^{-1}q_0\).
Together with (34), this proves

\[
                       (A^{-1}q_t)_1=t\mathcal K_t/2.
 \tag{35}
\]

The inverse rank-one update is

\[
 (A+s_0\mathbf e_1\mathbf e_1^T)^{-1}
 =A^{-1}-
 \frac{s_0A^{-1}\mathbf e_1\mathbf e_1^TA^{-1}}
      {1+s_0(A^{-1})_{11}}.
 \tag{36}
\]

The direct \(ww\) entry does not change. Substitute (34)--(35)
in (36) to obtain the first expression in (33); rearranging gives
the second. All denominators are strictly positive. \(\square\)

For the cap term in (22), use the pair \((e,z)\), \(t=1\),
and \(s_0=\Re\sigma\). The other change in its Hessian
is entirely in the private imaginary diagonal, so it does not
alter the column needed in this calculation. At a factorial
maximizer the [cap theorem](research_mixed_private_cap_curvature_bound.md)
gives \(s_0>68/45\). Substituting \(68/45\) for \(s_0\)
in (33) therefore gives a strict upper bound on its effective
curvature, without estimating the three factors in (33) separately.

For the ordinary term in (22), first eliminate the private variable
\(b\). Its relevant imaginary column has zero \(b\) entry,
so this elimination does not alter the remaining column. The pair
\((s,z)\) has \(t=-1\), and its additional private curvature is

\[
 s_0=(1+\epsilon)\Re p_s-\Re j
          -\frac{(\Re j)^2}{(1+\epsilon/2)\Re p_b-\Re j}>0.
 \tag{37}
\]

This is the positive real Schur complement of
\(\Phi_1(s,b)-\epsilon g(s)-\epsilon g(b)/2\).
Thus (33) computes the ordinary contribution exactly as well.
Combining these two contributions with (23) still requires the
shared-coordinate correction (21). In particular the individual
formulas are not a proof of the uniform six-pi bound.

## 8. The improved coordinate bounds still require stationarity

The coordinate and sign inequalities proved so far do not imply the
six-pi curvature bound at every point satisfying them. Here is one
explicit point for the next-type-three phase:

\[
 e=\frac{39}{100}-\frac{i}{50},\qquad
 s=\frac{49}{100}-\frac{3i}{50},\qquad
 z=\frac{23}{100}+\frac{i}{100},\qquad
 b=\frac{11}{25}-\frac{3i}{50}.
 \tag{38}
\]

It satisfies the strict coordinate restrictions, both actual ordinary
height intervals, the summed-real-part bound \(\Re(s+z)<.82\),
and the positive-height factorial cutoff \(\Re z<1/3\).
Its cap uses the original analytic branch (16); equivalently, use
\(\sigma=p_e+2(p_e^2+1)/\sqrt{(p_e+i)^2+4}\), with the
square root in the first quadrant. The positive real Hessian has
strictly positive pivots \(E_0,B_0,T_0,D_0\) in the exact
Schur formula. It also satisfies

\[
 \Re\sigma>\Re p_e+109/90,\qquad
 0<q_e<1,\quad -2<q_s<0,\quad 0<a_0<299/60.
 \tag{39}
\]

Nevertheless a single outward interval evaluation proves

\[
                 K_{\rm eff}/\pi>13/2>6,
                 \qquad \Re\mathcal F_s<-1.
 \tag{40}
\]

The [standalone scalar check](../experiments/check_mixed_curvature_coordinate_obstruction.py)
starts from the exact rational coordinates (38), uses 192-bit
outward ball arithmetic, and verifies the pivots, (39), and (40).
Its [saved result](../repro/results/research-mixed-curvature-coordinate-obstruction.json)
binds the checking script and records the enclosures. It evaluates
only elementary phase derivatives at this one point, with no root
solve, original finite-source evaluation, or parameter cover.

The last inequality in (40) explains why this does not contradict
the proposed bound at maximizing points: \(s\) is strictly
inside its original real interval, and a small decrease of
\(\Re s\) increases the objective. The fixed outgoing affine
subtraction affects only the \(b\) derivative, so it cannot
repair this failed stationary equation. Nor is the point asserted
to share its heights with the reference of any complete word.
Thus the example rules out a deduction from the present coordinate,
cap, and sign inequalities alone. It leaves the original
optimizer-constrained curvature problem open.
