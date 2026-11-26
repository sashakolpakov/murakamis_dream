# The left cap cut and the ordinary main contour for a next-four block

Research deduction, 6 November 2026.

The ordinary block of type four has one more index factorial than the
type-three block. Its contribution to the real Hessian is useful:
it increases the cost of moving the ordinary index below its original
critical value. The outgoing halfweight changes the marginal that
must be subtracted, but cancels from the trial action after that
marginal has been retained.

This note proves two explicit upper bounds for the left-cap/main-contour
comparison. Their signs on the full reference family remain to be
proved. No numerical calculation is used below.

## 1. The exact objective and its reference gradient

Use the original phases and actual references in the
[next-four finite reduction](research_mixed_selected_four_four_finite_reduction.md).
In particular, the word has length at least three, its first two
vertices have type four, and its later vertices have type three or four.
Write
\[
 \begin{gathered}
 e_0=.27,\qquad H=.01,\qquad P=[.22,.45],\\
 e_*=e_R^*+ih_e,\quad s_*=s_R^*+ih_s,\quad
 z_*=a+ic,\quad b_*=v_*+ih_b,\\
 -.102<h_s,h_b<-.001,\quad -.078<c<-.020,\quad
 .24<s_R^*,v_*<.36,\quad .246<a<.350 .
 \end{gathered}
 \tag{1}
\]
The phases, calibrated action, and outgoing marginal are
\[
 \begin{split}
 Q_4(s;z,b)&=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs,\\
 \mathcal F_4&=\Psi+Q_4-g(z)-\tfrac12g(b),\\
 M&=\Re\mathcal F_4(e_*,s_*;z_*,b_*),\\
 p&=g'(s_*+b_*)-\tfrac32g'(b_*),\qquad p_R=\Re p.
 \end{split}
 \tag{2}
\]
All primitives have their original logarithmic branches and additive
normalizations. In particular, the cap includes its original private
action.

For \(\nu=1\) (the factorial estimate) and \(\nu=0\) (the forced
estimate), put
\[
 \begin{split}
 f_\nu(x,y,v)={}&
 \Re\{\Psi(e_0,y+iH)+Q_4(x+ih_s;y+iH,v+ih_b)\}\\
 &-\tfrac12\Re g(v+ih_b)-\nu\Re g(y+iH)-2\nu\pi H
                 -p_R(v-v_*).
 \end{split}
 \tag{3}
\]
These are two estimates for the same complete selected Fourier
polynomial, with the original outgoing halfweight.

The maximum in the ordinary index can be restricted from
\([1/8,1/2]\) to \([.22,.5]\). Indeed, the lower-index barrier in
Section 2 of the
[next-four endpoint deduction](research_mixed_first_four_next_four_endpoint_budget.md)
uses only \(Q_{4,s}\), its monotonicity, and the ranges of \(z,b,h_s\).
The cap coordinate and the terms added in (3) do not enter this
derivative. Thus its proof, including the preceding exclusion of
\(x\le .2\), applies with the cap fixed at \(e_0\). Consequently
\[
 \sup_{y,v\in P}\{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}
      =\max_{[.22,.5]\times P^2} f_\nu-M .
 \tag{4}
\]
The profile \(B_0\) here includes the outgoing halfweight, as in the
finite reduction.

Set
\[
 \begin{gathered}
 S_*=e^{-2\pi is_*},\quad Z_*=e^{-2\pi iz_*},\quad
 E_0=e^{-2\pi ie_0},\quad z_H^*=a+iH,\\
 \lambda=e^{2\pi(H-c)},\qquad \ell=\log\lambda,\\
 d=\ell-\log\left|\frac{1-\lambda S_*Z_*}{1-S_*Z_*}\right|,\qquad
 \beta_\nu=\log\left|
 \frac{(1-\lambda E_0Z_*)(1-\lambda S_*Z_*)}
 {S_*(1-\lambda Z_*)^{2+\nu}}\right|.
 \end{gathered}
 \tag{5}
\]
Here \(d>0\). The reference pair satisfies
\(.545<\Re(s_*+z_*)<.71\), so \(\Re(S_*Z_*)<0\).
Since \(\lambda>1\), the identity
\[
 \lambda^2|1-T|^2-|1-\lambda T|^2
       =(\lambda-1)(\lambda+1-2\lambda\Re T)>0,
       \qquad T=S_*Z_*,
 \tag{6}
\]
proves the claim. The exact original critical equations give
\[
             \nabla f_\nu(s_R^*,a,v_*)=(-d,\beta_\nu,0).
 \tag{7}
\]
For the first component, the original value of \(Q_{4,s}\) is zero
and its change is the logarithmic increment minus \(\ell\).
The second component includes the chirp derivative
\(-\log|S_*|\). The third vanishes because (2) is the derivative
of the full allocated outgoing phase. In particular, discarding
the halfweight before computing the marginal would invalidate (7).

## 2. A pair estimate on the wider type-four height range

Let \(V(s,w)=g(s+w)-g(s)-g(w)\), and suppose
\[
 .22\le\Re s\le.5,\quad \Re w\in P,\qquad
 |\Im s|,|\Im w|\le.102 .
 \tag{8}
\]
Write \(a_s=\Re\cot\pi s\), \(a_w=\Re\cot\pi w\), and
\(C=\Re\cot\pi(s+w)\). The real horizontal Hessian is
\[
 -\pi^{-1}\Re V''=
 \operatorname{diag}(a_s,a_w)-C
                 \begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{9}
\]

**Lemma 1.** On (8),
\[
 -\pi^{-1}\Re V''\succeq\operatorname{diag}(0,a_w/2).
 \tag{10}
\]
If also \(\Im s=h_s\) and \(.22\le\Re s\le s_R^*\), then
\[
 -\pi^{-1}\Re V''\succeq
                   \operatorname{diag}(39/160,a_w/2).
 \tag{11}
\]

*Proof.* When \(C\le0\), the subtracted matrix in (9) is
nonnegative and \(a_s\ge0\), proving (10). On the smaller
fixed-height interval in (11), the real cotangent decreases with
\(\Re s\), so \(a_s\ge a_*:=\Re\cot\pi s_*>2/5\).
The last reference bound is proved in the
[correlated endpoint deduction](research_mixed_next_four_correlated_endpoint_budget.md).
This also proves (11) in the present case.

Suppose \(C>0\), so \(\Re(s+w)<.5\). Put
\(p_0=\cot(\pi\Re s)\) and \(q_0=\cot(\pi\Re w)\).
The elementary cotangent bound at \(.22\pi\), also used in the
[next-three pair estimate](research_mixed_selected_cap_left_main_majorant.md),
gives
\[
 0<p_0,q_0<5/4,\qquad 1<p_0q_0<25/16 .
 \tag{12}
\]
The bounds \(\cos(.44\pi)<1/5\) and
\(\cosh(.204\pi)<49/40\) imply
\[
 a_s\ge\tfrac34p_0,\qquad a_w\ge\tfrac34q_0,\qquad
 C\le c_0:=\frac{p_0q_0-1}{p_0+q_0}.
 \tag{13}
\]
Indeed, the ratio of a complex real cotangent to its real-axis value
is \((1-c_0')/(\cosh\eta-c_0')\), with \(c_0'\le1/5\).
It is at least \(32/41>3/4\). The cosine bound follows already
from \(\cos(.44\pi)=\sin(.06\pi)<.06(22/7)<1/5\);
the cited endpoint deductions prove the hyperbolic-cosine bound.

After reserving \(a_w/2\) in the second direction, (9) is at least
\[
 N=\operatorname{diag}(3p_0/4,3q_0/8)
                      -c_0\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{14}
\]
Let \(\alpha=3p_0/4\), \(\beta=3q_0/8\). Then
\[
 \begin{split}
 \beta-c_0&=\frac{3q_0^2-5p_0q_0+8}{8(p_0+q_0)}>0,\\
 \alpha\beta-(\alpha+\beta)c_0
 &=\frac{3\{4(2p_0+q_0)-p_0q_0(5p_0+q_0)\}}
                {32(p_0+q_0)}\\
 &\ge\frac{3(3p_0+39q_0)}{512(p_0+q_0)} .
 \end{split}
 \tag{15}
\]
The Schur remainder is therefore at least
\[
 \frac{\alpha\beta-(\alpha+\beta)c_0}{\beta-c_0}
 \ge\frac{3p_0+39q_0}{64q_0(p_0+q_0)}
 \ge\frac{39}{64(p_0+q_0)}\ge\frac{39}{160}.
 \tag{16}
\]
This proves both assertions when \(C>0\).
For the monotonicity used when \(C\le0\), differentiating the
real cotangent gives a negative derivative whenever
\(\cosh(2\pi h_s)\cos(2\pi\Re s)<1\), which holds on
\([.22,.36]\) by the same bounds. \(\square\)

## 3. The two scalar bounds

At the incoming height \(H=.01\), the bounds already used in the
[next-three left-cut comparison](research_mixed_selected_cap_left_main_majorant.md)
give
\[
 a_z>3/20,\qquad \Re\cot\pi(e_0+z)<1/30.
 \tag{17}
\]
Thus the cap contributes more than \(7\pi/60\) in the incoming
direction. The pair \(V(s,z)\) contributes at least \(\pi a_z/2\),
and the Fourier term contributes \(\nu\pi a_z\).
The outgoing direction has a positive remaining curvature:
the pair and the halfweight together contribute \(\pi a_b>0\).

Set
\[
 \mu_\nu=\frac{(23+18\nu)\pi}{120},\qquad
 \mu_s=\pi(39/80+a_*),\qquad a_*=\Re\cot\pi s_*>2/5.
 \tag{18}
\]
In particular \(\mu_s>71\pi/80\). Since
\[
 Q_4=V(s,z)+V(s,b)-g(s)+2\pi izs,
 \tag{19}
\]
Lemma 1 gives a global real Hessian lower bound with zero first
entry and incoming entry \(\mu_\nu\). On the portion
\(x\le s_R^*\), its first entry improves to \(\mu_s\):
the two pair terms contribute \(39\pi/80\), and the additional
\(-g(s)\) contributes at least \(\pi a_*\).
The chirp has zero real horizontal Hessian.

For \(l\le0\le r\), write
\[
 \Gamma_\mu(t;l,r)=\max_{l\le h\le r}(th-\mu h^2/2).
 \tag{20}
\]
Its maximizer is \(\operatorname{clip}(t/\mu,l,r)\). Define
\[
 \begin{split}
 \mathcal L_\nu={}&
 \Re\{\Psi(e_0,z_H^*)-\Psi(e_*,z_*)\}\\
 &+\Re\{g(s_*+z_H^*)-g(s_*+z_*)-g(z_H^*)+g(z_*)
                         +2\pi is_*(z_H^*-z_*)\}\\
 &+\Re g(z_*)-\nu\Re g(z_H^*)-2\nu\pi H,\\
 \mathcal J_\nu^{(4)}={}&\mathcal L_\nu
       +\Gamma_{\mu_s}(-d;.22-s_R^*,0)
       +\Gamma_{\mu_\nu}(\beta_\nu;.22-a,.45-a).
 \end{split}
 \tag{21}
\]

**Theorem 2.** On the actual reference family (1),
\[
 \sup_{y,v\in P}\{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}
             \le\mathcal J_\nu^{(4)},\qquad \nu=0,1.
 \tag{22}
\]

*Proof.* The trial value \(f_\nu(s_R^*,a,v_*)-M\) is exactly
\(\mathcal L_\nu\). The outgoing halfweight and the additional
index factorial occur at the same unchanged reference coordinates
in both values and cancel there; their derivatives and curvatures
have already been included in (7) and (18).

Integrate the real Hessian estimate along the segment from the
trial point to a target. If \(x\le s_R^*\), its first linear and
quadratic terms are bounded by the first gain in (21). If
\(x\ge s_R^*\), its first linear term is nonpositive because
\(d>0\), and the global zero first curvature is sufficient.
The outgoing linear term is zero; its quadratic term can be
discarded because it is nonpositive. Maximizing the incoming
quadratic term gives the second gain. Equation (4) proves (22).
\(\square\)

The action difference in (21) retains \(S(.27)-S(e_*)\) and both
original cap chirps. It is evaluated at the same endpoint parameter
as the reference gradients and curvatures. The additional type-four
factorial has changed the index gain, not the displayed trial action.

The unproved numerical assertion is
\[
           \max(\mathcal J_0^{(4)},\mathcal J_1^{(4)})<-\delta
 \quad\text{uniformly on the required reference family},
 \qquad\delta>0.
 \tag{23}
\]
It must use the next-four rational maps and necessary reference
conditions. The next-three parameter test cannot be substituted.
Even a proof of (23) would settle only the pair \((L,0)\) in the
five-pair finite reduction; the half-row and ordinary-left-cut
comparisons remain separate.
