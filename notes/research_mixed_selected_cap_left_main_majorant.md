# Two scalar majorants for the left cap cut with the ordinary main contour

Research deduction, 6 November 2026. The left cap cut can be compared
jointly with the neighboring main contour without replacing the cut
by the cap's main profile. The outgoing tangent cancels its target
gradient at the original reference. The conditional-index gradient
has a proved negative sign, allowing a stronger quadratic cost only
in the direction in which its linear term can increase.

The result below removes all three real integration targets and gives
two explicit scalar upper bounds on the original correlated reference
family. Their uniform signs are not established here. No root,
source sum, parameter cover or previous certificate is evaluated.

## 1. Literal phase, reference, and target gradients

Keep the actual first-four/next-three reference, complete cap phase
\(\Psi\), ordinary phase \(Q\), action \(M\), outgoing
marginal \(p\), and affine term \(\ell_b\) from
[the finite-source reduction](research_mixed_selected_four_three_finite_reduction.md).
Write
\[
 \begin{gathered}
 e_0=27/100,\quad H=7/625,\quad
 e_*=e_R^*+ih_e,\quad s_*=s_R^*+ih_s,\quad
 z_*=a+ic,\quad b_*=v_*+ih_b,\\
 -.065<h_s,h_b<.068,\quad -.070<c<-.020,\\
 .267<s_R^*,v_*<.433,\quad .246<a<.350,
 \quad P=[.22,.45].
 \end{gathered}
\tag{1}
\]
The next vertex is ordinary even when its next external input is an
attached endpoint in a word of length three. These reference bounds
are the original open-word bounds, not cyclic replacements.

For \(\nu=1\) (factorial) or \(\nu=0\) (forced), define
the real target objective
\[
 \begin{split}
 f_\nu(x,y,v)={}&
 \Re\{\Psi(e_0,y+iH)+Q(x+ih_s;y+iH,v+ih_b)\}\\
 &-\nu\Re g(y+iH)-2\nu\pi H-p_R(v-v_*),
 \qquad p_R=\Re p.
 \end{split}
\tag{2}
\]
The two alternatives in (2) bound the same complete selected Fourier
polynomial. There is no division by a halfweight.

The maximum over the original \(x\in[.15,.5]\) can be
restricted to \([.2,.5]\), for both alternatives. Indeed the
lower-index barrier in Proposition 4 of
[the height-envelope proof](research_mixed_selected_boundary_height_envelope.md)
uses only the original marginal
\[
 Q_s=g'(s+z)+g'(s+b)-2g'(s)+2\pi iz.
\tag{3}
\]
It is independent of the private cap coordinate, the Fourier
alternative, and the outgoing affine subtraction. The proof excludes
\(\Re s\le.2\) for every \(y,v\in P\), at the heights
in (1), and hence also with \(e=e_0\) fixed. Consequently
\[
 \sup_{y,v\in P}
 \{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}
       =\max_{[.2,.5]\times P^2}f_\nu-M.
\tag{4}
\]

Set
\[
 E_0=e^{-2\pi i e_0},\quad S_*=e^{-2\pi is_*},\quad
 Z_*=e^{-2\pi iz_*},\quad z_H^*=a+iH,\quad
 \lambda=e^{2\pi(H-c)},\quad \ell=\log\lambda,
\tag{5}
\]
and define
\[
 \begin{split}
 d&=\ell-
       \log\left|\frac{1-\lambda S_*Z_*}{1-S_*Z_*}\right|>0,\\
 \beta_\nu&=
 \log\left|
 \frac{(1-\lambda E_0Z_*)(1-\lambda S_*Z_*)}
        {S_*(1-\lambda Z_*)^{2+\nu}}
 \right|.
 \end{split}
\tag{6}
\]
The sign \(d>0\) is the correlated increment inequality
(23)--(25) of
[the endpoint Legendre proof](research_mixed_selected_endpoint_legendre_budget.md).
It uses the actual \(S_*Z_*\), rather than independent extrema
of the two factors. The exact gradient at the original real trial is
\[
             \nabla f_\nu(s_R^*,a,v_*)=(-d,\beta_\nu,0).
\tag{7}
\]
For the first component use \(Q_s(s_*;z_*,b_*)=0\)
and retain the chirp's change \(-\ell\). For the second,
\(\Psi_z=g'(e+z)-g'(z)\), and the same chirp contributes
\(-\log|S_*|\), the denominator in (6). The final component
vanishes because
\(p=g'(s_*+b_*)-g'(b_*)\), independently of \(z\).
Thus the outgoing coordinate is retained in the comparison, with its
original marginal canceled exactly.

## 2. A directional ordinary-pair curvature estimate

Let \(V(s,w)=g(s+w)-g(s)-g(w)\), with
\[
 .2\le\Re s\le.5,\quad \Re w\in P,
 \qquad |\Im s|,|\Im w|\le.068.
\tag{8}
\]
Write \(a_s=\Re\cot\pi s\), \(a_w=\Re\cot\pi w\),
and \(C=\Re\cot\pi(s+w)\). Then
\[
 -\pi^{-1}\Re V''=
 \operatorname{diag}(a_s,a_w)-C
               \begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{9}
\]

**Lemma 1.** Throughout (8),
\[
 -\pi^{-1}\Re V''\succeq\operatorname{diag}(0,a_w/2).
\tag{10}
\]
If additionally \(\Re s\le s_R^*<.433\), then
\[
 -\pi^{-1}\Re V''\succ\operatorname{diag}(1/5,a_w/2).
\tag{11}
\]
If in addition \(\Im s=\Im s_*\), one may replace
\(1/5\) in (11) by
\(\delta_*:=\min\{\Re\cot\pi s_*,15/53\}>1/5\),
with a nonstrict inequality if required. This extra fixed-height
hypothesis is needed only for the stronger version.

*Proof.* If \(C\le0\), (9) is the sum of a nonnegative
rank-one matrix and \(\operatorname{diag}(a_s,a_w)\).
Here \(a_s\ge0\). On \([.2,s_R^*]\subset[.2,.433]\),
the uniform bound \(a_s>1/5\) is proved in (29) of the
cited Legendre note, using \(\cosh(.136\pi)<11/10\).
For the stronger version, keep \(\Im s=\Im s_*\).
The real cotangent then decreases with the real coordinate, giving
\(a_s\ge\Re\cot\pi s_*\).

Suppose \(C>0\). Then \(\Re(s+w)<.5\). Put
\(p=\cot(\pi\Re s)\), \(q=\cot(\pi\Re w)\).
The elementary real bounds are
\[
 0<p<7/5,\qquad 0<q<5/4,\qquad
 pq>1,\qquad pq<7/4.
\tag{12}
\]
For the upper bounds, use monotonicity of cotangent and the sine
cubic/cosine quartic at \(157/250<\pi/5\) and
\(69/100<.22\pi\), respectively. At both rational angles
the corresponding sine lower bound times \(7/5\) or \(5/4\)
exceeds the cosine upper bound. The condition \(pq>1\)
is the real addition formula when \(\Re(s+w)<.5\).

The exact cotangent formula and \(\cosh(.136\pi)<11/10\)
give
\[
 a_s\ge\frac67p,\qquad a_w\ge\frac67q,
 \qquad C\le c_0:=\frac{pq-1}{p+q}.
\tag{13}
\]
For the first two inequalities, the reduction factor from a real
cotangent is \((1-c)/(\cosh\eta-c)\), where
\(c\le\cos(.4\pi)<1/3\); this exceeds \(6/7\).
Therefore subtracting \(\operatorname{diag}(0,a_w/2)\)
from (9) leaves a matrix at least
\[
 N=\operatorname{diag}(6p/7,3q/7)
                 -c_0\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{14}
\]
Its lower-right entry is positive, since
\[
 \frac{3q}{7}-c_0
   =\frac{3q^2-4pq+7}{7(p+q)}>0.
\tag{15}
\]
Writing \(\alpha=6p/7\), \(\beta=3q/7\), its
Schur remainder in the first coordinate is
\[
 \begin{split}
 \frac{\alpha\beta-(\alpha+\beta)c_0}{\beta-c_0}
 &\ge\frac{3}{4(p+q)}\ge\frac{15}{53}>\frac15,\\
 \alpha\beta-(\alpha+\beta)c_0
 &=\frac{3\{7(2p+q)-pq(8p+q)\}}{49(p+q)}
   \ge\frac{9q}{28(p+q)}.
 \end{split}
\tag{16}
\]
The second line uses \(pq\le7/4\); the first also uses
\(\beta-c_0\le\beta\) and \(p+q\le53/20\).
This proves (10)--(11), including the stated stronger remainder.
\(\square\)

On the whole outer interval \(P\) at heights at most \(.068\),
\[
                         a_w>3/20.
\tag{17}
\]
This is the elementary cotangent bound (30) of the Legendre note;
the same proof applies throughout \(P\), since the real cotangent
decreases there. At the fixed left cut, the summed real part is
\(e_0+y\in[.49,.72]\), so
\(\Re\cot\pi(e_0+z)<1/30\). The bare cap contributes
\[
 -\partial_y^2\Re\Psi(e_0,y+iH)
 =\pi\{a_z-\Re\cot\pi(e_0+z)\}>7\pi/60.
\tag{18}
\]
Its constant private action contributes no derivative.

## 3. Two explicit scalar tests

Put
\[
 \mu_\nu=\frac{(23+18\nu)\pi}{120},\qquad
 \mathcal L_\nu=f_\nu(s_R^*,a,v_*)-M.
\tag{19}
\]
For an interval \(l\le0\le r\), let
\(\Gamma_\mu(p;l,r)\) be the exact maximum of
\(pt-\mu t^2/2\) on that interval, namely its value at
\(t=\operatorname{clip}(p/\mu,l,r)\). Define
\[
 \mathcal J_\nu=
 \mathcal L_\nu+
 \Gamma_{2\pi/5}(-d;\ .2-s_R^*,\ 0)
 +\Gamma_{\mu_\nu}(\beta_\nu;\ .22-a,\ .45-a).
\tag{20}
\]

**Theorem 2.** For each \(\nu=0,1\),
\[
 \sup_{y,v\in P}
 \{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}
                         \le\mathcal J_\nu.
\tag{21}
\]
The stronger index curvature \(2\pi\delta_*\) from
Lemma 1 may replace \(2\pi/5\) in (20).

*Proof.* Write the ordinary phase as
\(V(s,z)+V(s,b)+2\pi izs\). Its chirp has zero real
horizontal Hessian. Apply (10) to both pairs, (17)--(18) to
the outer directions, and retain the additional \(-\nu g(z)\)
from the actual Fourier alternative. On the whole target box this
gives
\[
 -\nabla^2 f_\nu\succeq
                \operatorname{diag}(0,\mu_\nu,3\pi/40).
\tag{22}
\]
On its portion \(x\le s_R^*\), (11) improves the first
diagonal entry to \(2\pi/5\).

For any target, integrate this matrix lower bound along the straight
segment from \((s_R^*,a,v_*)\). If \(x\le s_R^*\),
the entire segment has the stronger first diagonal entry; if
\(x\ge s_R^*\), its first linear contribution
\(-d(x-s_R^*)\) is already nonpositive and the zero first
curvature suffices. The outgoing linear contribution is exactly
zero by (7), while its remaining quadratic term is nonpositive.
Taking the maximum of the two possible index contributions therefore
gives precisely the first clipped gain in (20). Maximizing the
independent incoming quadratic gives the second. Equation (4)
now proves (21). This argument does not assert which direction the
true coupled optimizer chooses. The stronger version follows from
the final statement of Lemma 1. \(\square\)

The trial action in (19) preserves the private action difference.
For clarity it can be evaluated as
\[
 \begin{split}
 \mathcal L_\nu={}&\Re\{\Psi(e_0,z_H^*)-\Psi(e_*,z_*)\}\\
 &+\Re\{g(s_*+z_H^*)-g(s_*+z_*)-g(z_H^*)+g(z_*)
                         +2\pi is_*(z_H^*-z_*)\}\\
 &+\Re g(z_*)-\nu\Re g(z_H^*)-2\nu\pi H.
 \end{split}
\tag{23}
\]
In the first line, the difference contains exactly
\(S(.27)-S(e_*)\), with \(e_*\) at its unchanged
actual complex height. Its expansion is equation (13) of
[the half-row evaluation specification](research_mixed_selected_half_row_evaluation_design.md).
No private height is reset and no imaginary tangent is discarded.

All inputs in (6), (19)--(23) are functions of the same original
complex endpoint parameter \(U=e^{2\pi iu_*}\), with the
rational maps and actual branch/domain restrictions of the central
scalar proof. A sufficient remaining comparison is
\[
                    \max(\mathcal J_0(U),\mathcal J_1(U))< -\delta
\tag{24}
\]
for some \(\delta>0\) on that admitted reference family.
This note does not prove (24), nor does it replace correlated
increments, actions and slopes by independently optimized ranges.
Together with separately proved half-row comparisons, such a result
would close the three-profile finite reduction; without their signs
it remains a quantitative upper-bound theorem.
