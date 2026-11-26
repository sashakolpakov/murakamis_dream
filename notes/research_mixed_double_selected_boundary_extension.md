# One outgoing response for the two selected coordinates

Research deduction, 6 November 2026. Including the original first cap
removes the incoming boundary response from the second-selection
comparison. The remaining simultaneous-selection profiles have only
the outgoing response \(p_R'b_*'\). Its modulus is already present
in the completed reference records. This note proves the extension
identity and a sufficient boundary test. It supplies no new numerical
boundary signs.

## 1. The original six-variable phase and its stationary reference

Fix first three flags \((1,1,\beta)\), \(\beta\in\{0,1\}\),
in an actual mixed open word of length \(m\ge4\). Use the canonical
family of the [reference-curve theorem](research_mixed_second_selected_reference_curve.md),
parametrized by the next external leg \(c=s_4^*\). The seven original
coordinates are \((e_*,\xi_*,a_*,u_*,z_*,v_*,b_*)\).
At length four \(c\) is attached; at larger lengths it is ordinary.
It is never a private terminal leg.

The first endpoint packet gives its original holomorphic stationary
action \(S(e)\), with auxiliary coordinate \(\xi=u_c(e)\).
Keep the cap phase and bare ordinary phases exactly as in the
[finite first-four/next-four reduction](research_mixed_selected_four_four_finite_reduction.md):
\[
 \begin{split}
 \Psi_{\rm cap}(e,a)
   &=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q_\epsilon(s;a,b)
   &=g(s+a)+g(s+b)-(2+\epsilon)g(s)-g(a)-g(b)+2\pi ias,\\
 F_{123}(e,a,u,z,v,b)
   &=\Psi_{\rm cap}(e,a)+Q_1(u;a,z)+Q_\beta(v;z,b)
                  -g(a)-g(z)-\frac\beta2g(b).
 \end{split}
 \tag{1}
\]
Here \(g\) has its original branch and additive normalization.
In particular \(S\) is not replaced by a new root or an independently
calibrated phase. The reference \(\xi_*\) is the same canonical
auxiliary solution at \(e_*\).

In the order \(r(c)=(e_*,a_*,u_*,z_*,v_*,b_*)\), the original
equations imply
\[
 F_e(r)=F_a(r)=F_u(r)=F_z(r)=F_v(r)=0,\qquad
 F_b(r)=p_R(c)=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \tag{2}
\]
Indeed eliminating \(\xi\) in the original endpoint action retains
its envelope derivative. The \(e,a\) rows then are the two original
endpoint matching equations, and the \(u,z,v\) rows are the
unchanged ordinary and retained-coordinate equations. Equivalently,
the two original allocated derivatives at \(a\) cancel after
the cap is restored, just as the two derivatives at \(z\) cancel.
Thus there is no remaining \(p_L\) term in (2).

All of (2) holds holomorphically on the canonical neighborhood,
not just at one word reference. The next parameter belongs to
\[
 \begin{split}
 K_3={}&\{|c-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im c\le.068,\ \Re c-3\Im c\le.608\},\\
 K_4={}&\{|c-(.30-.052i)|\le.060\}
       \cap\{-.108\le\Im c\le-.001\}.
 \end{split}
 \tag{3}
\]
The existing canonical theorem supplies existence and holomorphy on
neighborhoods of these sets. They may contain parameters not realized
by a finite word; the same stationary equations still apply.

## 2. Constant formal coordinates for the cap cut and the half row

Put \(H=1/100\), \(P=[.22,.45]\), and
\[
 \mathcal X_\beta=[.27,.49]\times P\times[.125,.5]
                      \times P\times[\ell_\beta,.5]\times P,
 \qquad \ell_0=.15,\quad\ell_1=.125.
 \tag{4}
\]
Let \(j\in\{0,L\}\) select the cap main line or its real left
cut. Let \(k\in\{0,R\}\) select the outgoing main line or
its real half row. Only \(k=0\) remains necessary for \(\beta=1\),
by the completed outgoing-four half-row domination. Define the
holomorphic coordinate substitution
\[
 \iota_{j,k}(w)_e=
   \begin{cases}w_e,&j=0,\\.27,&j=L,\end{cases}
 \qquad
 \iota_{j,k}(w)_v=
   \begin{cases}w_v,&k=0,\\1/2,&k=R,\end{cases}
 \tag{5}
\]
with the other four coordinates unchanged. Thus the substituted
function is independent of any formal fixed coordinate.
For \(\nu_1,\nu_2\in\{0,1\}\), where one is factorial and
zero is forced, set
\[
 \widehat\Psi_{j,k,\nu_1,\nu_2}(w)
   =F_{123}(\iota_{j,k}(w))+(1-\nu_1)g(w_a)
       +(1-\nu_2)g(w_z)+2\pi i(\nu_1w_a+\nu_2w_z).
 \tag{6}
\]
Neither selected Fourier polynomial is split or divided out.
The four choices in (6) are upper-rate alternatives for their exact
product.

Let \(\lambda_e=1\) for \(j=0\) and zero for \(j=L\);
let \(\lambda_v=1\) for \(k=0\) and zero for \(k=R\). With
\[
 \Lambda_{j,k}=\operatorname{diag}(\lambda_e,0,1,0,\lambda_v,1),
 \qquad h=(0,H,0,H,0,0),\qquad
 w=x+ih+\tfrac12\Lambda_{j,k}(r-\bar r),
 \tag{7}
\]
use \(x\in\mathcal X_\beta\), fixing \(x_e=.27\) or
\(x_v=.5\) when appropriate. Define the literal profile defect
\[
 D_{j,k,\nu_1,\nu_2}(c;x)
 =\Re\{\widehat\Psi_{j,k,\nu_1,\nu_2}(w)-F_{123}(r)
                                     -p_R(c)(w_b-b_*)\}.
 \tag{8}
\]
Because of (2), the affine subtraction in (8) equals
\(F_{123}'(r)\cdot(w-r)\), even on a fixed cap cut or half row.
The reference action still uses the actual \(e_*,v_*\); only the
target phase has a constant formal coordinate. In particular the
original half-row constant and the reference \(g(v_*)\) are retained.

The needed height bounds are
\[
 \begin{gathered}
 -.051<\Im e_*<-.019,\qquad -.102<\Im u_*<-.001,\\
 (\Im v_*,\Im b_*)\in
 \begin{cases}(-.065,.068)^2,&\beta=0,\\
 (-.102,-.001)^2,&\beta=1.
 \end{cases}
 \end{gathered}
 \tag{9}
\]
They hold on the whole canonical domains, from the original typed
images and the completed height-extension argument. On the main
cap line, \(w_e\) lies in
\([.27,.49]+i[-.055,.04]\); the fixed cut does too. All ordinary
and pair arguments remain in the original regular strip. For example
the cap sum has real part in \([.49,.94]\), and an ordinary
sum lies in \([.345,.95]\).

The [bare cap Hessian bound](research_mixed_first_cap_plateau_phase.md),
Lemma 1, holds throughout this cap product, including selected
\(\Im w_a=H\). The bare ordinary bounds in Section 2 of
[horizontal concavity](research_mixed_second_selected_horizontal_concavity.md)
hold on the full index intervals (4), with both selected outer
heights and with a real half row. Adding them and the nonnegative
own-coordinate contributions gives
\[
                  -\Re\widehat\Psi_{j,k,\nu_1,\nu_2}''\succeq0.
 \tag{10}
\]
Fixed formal rows and columns vanish; on the remaining variables
the inequality is strict. Indeed after adding the two Fourier
terms the own terms outside the bare blocks are precisely
\(-\nu_1g(a)-\nu_2g(z)-\beta g(b)/2\), whose negative real
Hessians are nonnegative. All chirps stay unchanged. The companion
[concave-profile budget](research_mixed_double_selected_concave_profile_budget.md)
records this same block argument and its rational-trial support test.

## 3. Only the outgoing boundary response survives

**Proposition 1.** For each fixed target and each of the profiles
above, the original defect satisfies
\[
 \begin{split}
 \Delta_cD
  &=-\Re\{(\Lambda_{j,k}r')^T
                \widehat\Psi''(w)\Lambda_{j,k}\bar r'\}
                           +2\Re\{p_R'\overline{b_*'}\}\\
  &\ge-2B_R(c),\qquad B_R(c)=|p_R'(c)b_*'(c)|.
 \end{split}
 \tag{11}
\]
The function \(B_R\) is subharmonic, independent of the target,
profile and Fourier alternative.

*Proof.* Apply the exact stationary-reference Laplacian identity
to (8), using (2), (7) and (10). All five internal response rows
vanish; the remaining boundary coefficient is \(\lambda_b=1\).
The modulus in (11) is that of a holomorphic product, so is
subharmonic. No second reference derivative or optimizer derivative
is used. \(\square\)

With \(k(t)=\pi\cot\pi t\), the exact outgoing derivative is
\[
 p_R'=[k(v_*+b_*)-i\pi]v_*'
       +[k(v_*+b_*)-(1+\beta/2)k(b_*)+i\pi\beta/2]b_*'.
 \tag{12}
\]
These are exactly the unchanged outgoing coefficients in the
[existing response provider](../experiments/mixed_second_selected_external_response.py).
Its saved fields `right_product` and `right_product_modulus` enclose
\(p_R'b_*'\) and \(B_R\), respectively. They can be consumed
from the completed source-linked reference bank without a new root,
inverse Jacobian or derivative evaluation. A recorded bound on the
old sum \(|p_L'a_*'|+|p_R'b_*'|\) is also a valid, weaker bound
for (11). An individual saved boundary interval is not by itself a
global bound.

**Corollary 2 (complete-boundary test).** On every part of
\(\partial K_\sigma\), suppose all required profiles and targets
satisfy \(D\le-\gamma\), and independently \(B_R\le B_0\).
Then throughout \(K_\sigma\),
\[
 D\le-\gamma+\frac{B_0R_\sigma^2}{2},\qquad
 \frac{R_3^2}{2}=\frac{6889}{2000000},\quad
 \frac{R_4^2}{2}=\frac9{5000}.
 \tag{13}
\]
In particular a strict positive corrected gap proves all those
profile signs uniformly in the whole external domain.

*Proof.* Subharmonicity extends the whole-boundary bound for \(B_R\)
to the interior. Subtract
\(q(c)=B_0(R_\sigma^2-|c-c_\sigma|^2)/2\) from the original
defect. By (11), \(D-q\) is subharmonic, and \(q\ge0\) on
the entire clipped disk, including every straight boundary segment.
The maximum principle proves (13). Phase minima and response maxima
must be taken separately over the complete boundary. \(\square\)

There is also the signed alternative. Choose one canonical anchor
\(r^0\) and put
\[
 C_0(c)=\tfrac12\Re\{[p_R(c)-p_R(c^0)]
                                      \overline{b_*(c)-b_*(c^0)}\}.
 \tag{14}
\]
Then \(D-C_0\) is subharmonic. Moreover \(C_0\le0\): the bare
cap and ordinary Hessian bounds also apply on the convex containing
product of actual references; their sum and the own terms make
\(-\Re F_{123}''\succeq0\). All five internal gradients vanish
at the two reference endpoints. The centered energy identity thus
gives this sign. Consequently a full-boundary inequality
\(d(c)-C_0(c)\le-\delta\), with \(D(c;x)\le d(c)\), implies
\(D\le-\delta\) inside. The positive boundary cost \(-C_0\)
cannot be discarded. No such signed boundary comparison or anchor
evaluation is supplied here.

## 4. Integration with the complete finite-current reduction

For \(\beta=0\), (8) contains the sixteen remaining profiles;
for \(\beta=1\), its main outgoing case contains the eight
remaining profiles of
[the double-selected last-row reduction](research_mixed_double_selected_last_rows.md).
A uniform positive gap \(\delta\) from (13), or from the signed
test, would insert directly into that reduction to give, for the
literal weighted three-factor product and every fixed color-jet order,
\[
 \mathcal B_{123,N}^{(k)}
 \le C_{\tau,k}N^{A_{\tau,k}}
  \exp N\{\Lambda_{123}-\min(3/1000,\delta)+\tau\}.
 \tag{15}
\]
The original outgoing modulus halfweight, complex marginal, cap
color and both level parities are those of that finite reduction.
The complete selected weights \(d_N(X_1)X_1^{-N}\) and
\(d_N(X_2)X_2^{-N}\) remain present. One arbitrary total tolerance
absorbs the existing finite-source and color estimates.

Formula (15) is conditional on new complete-boundary profile bounds.
The old single-selection scalar gaps do not provide them, and
double-precision maximizers at reference midpoints are not upper
bounds. A fixed rational trial and a proved full-box concavity bound
can supply a certified boundary majorant, as in the companion note;
that majorant itself is never differentiated in the extension.
No simultaneous-selection source theorem, nonplateau estimate or
whole-invariant conclusion is asserted here.
