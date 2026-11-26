# A global pre-Gram curve for every positive mixed prefix

Research deduction, 7 November 2026. Every nonempty positive word in
the original powers three and four has one global, unramified
following-reference sheet on the same two typed input disks. Both its
last leg and its initial auxiliary parameter are one-to-one coordinates
on that sheet. Removing precisely the final Gram incidence defines
the absolute pre-Gram action on the entire last-leg image. The last-leg
derivative has bounds independent of the word and its length.
This extends the sheet argument for
[the \(34\) prefix](research_mixed_three_four_following_critical_curve.md);
it does not prove a finite-source asymptotic or a remainder sign for a
new word. No numerical evaluation is used.

## 1. The original action and the common following domain

Fix \(m\ge1\), \(\epsilon_j\in\{0,1\}\), and the word
\(w=(3+\epsilon_1,\ldots,3+\epsilon_m)\). Retain the primitives
and constants of [absolute calibration](research_mixed_geometric_action_calibration.md):
\[
 \begin{split}
 g(z)&=J(z)+\frac{i\pi}{2}(z-z^2),\\
 E(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)
                  +i\pi eu-\frac{i\pi}{2}(e-e^2),\\
 V_\epsilon(s,t)&=g(s+t)-\epsilon\{g(s)+g(t)\},\\
 G(t,c)&=g(t+c)-2g(t)-2g(c)+2\pi itc.
 \end{split}                                                    \tag{1}
\]
For a following Gram coordinate \(c\), put
\[
 \begin{split}
 \mathcal A_w(z;c)
 &=E(s_1,u)+\sum_{j=1}^mV_{\epsilon_j}(s_j,t_j)
       +\sum_{j<m}G(t_j,s_{j+1})+G(t_m,c),\\
 z&=(u,s_1,t_1,s_2,t_2,\ldots,s_m,t_m),\\
 D_3&=\{|c-(.35-.01i)|\le.09\},\\
 D_4&=\{|c-(.30-.052i)|\le.064\},\qquad
 \Omega=D_3^\circ\cup D_4^\circ .
 \end{split}                                                    \tag{2}
\]
In particular \(c\) is not an ordinary terminal cap or an outgoing
Fourier wire coordinate.

[Cap-phase entrance, Lemma 1](research_mixed_alternating_cap_phase_entrance.md)
applies to every such word, not only to an alternating word. It supplies
a unique original-log critical point \(z_w(c)\) near each closed disk.
The two branches agree on the overlap. Its common larger convex product
is
\[
 \begin{split}
 u&\in\mathcal U=[.21,.25]+i[.01,.10],\\
 s_1&\in\mathcal E=[.33,.47]+i[-.09,.08],\\
 t_1,s_2,t_2,\ldots,s_m,t_m
     &\in Q=[.23,.45]+i[-.12,.12].
 \end{split}                                                    \tag{3}
\]
The roots have the stricter original typed image inclusions. The
Hessian estimate holds throughout (3), with \(c\) in either disk:
\[
 -\Re \mathcal A_{w,zz}''\succ\mu I,\qquad
 \mu=\frac{6\pi}{49},\qquad
 \|\mathcal A_{w,zz}''\|_2\le C_H,                              \tag{4}
\]
where \(C_H\) is independent of \(m,w\). Here the real part is the
Hermitian part; for a complex symmetric Hessian it equals the matrix
of entrywise real parts. The original
[convex-domain proof](research_mixed_open_word_hessian.md) justifies
the segment comparisons below. When \(m=1\), (3) consists of
\((u,s_1,t_1)\), and the original single-endpoint map is exactly the
required existence theorem.

Write
\[
 q_w(c)=t_m(c),\quad
 U_w(c)=e^{2\pi i u(c)},\quad
 C(c)=e^{-2\pi ic},\quad H_w(c)=\mathcal A_w(z_w(c);c).
                                                               \tag{5}
\]
The positive sign in \(U_w\) is the convention of the original rational
transport. It is the reciprocal of the auxiliary exponential used in
the special \(34\) following-curve note.

## 2. Rational reconstruction on the already selected sheet

For clarity, the required algebra is recorded with its original
nonvanishing conditions. Define the existing rational initializer
\[
 \begin{split}
 \mathcal E_0(U)&=\frac{(1+U)^2}{1-2U+5U^2},\\
 Z_\alpha(U)&=
 \frac{1-(1-\mathcal E_0(U)U)(1-\mathcal E_0(U))^\alpha/U}
       {\mathcal E_0(U)},\\
 S_\alpha(U)&=
 \frac{1-\mathcal E_0(U)Z_\alpha(U)}
 {Z_\alpha(U)(1-\mathcal E_0(U)Z_\alpha(U))
                         +(1-Z_\alpha(U))^{2+\alpha}} .
 \end{split}                                                    \tag{6}
\]
These are [rational critical transport, equation (3)](research_mixed_rational_critical_transport.md),
deduced there from the original endpoint equations. Set
\[
 S_j=e^{-2\pi i s_j},\qquad T_j=e^{-2\pi i t_j}.
\]
At the critical point,
\[
 S_1=\mathcal E_0(U_w),\qquad T_1=Z_{\epsilon_1}(U_w).
                                                               \tag{7}
\]
For \(m=1\), the final external exponential is simply
\[
                  C=\mathcal C_w(U_w):=S_{\epsilon_1}(U_w).
                                                               \tag{8}
\]
For \(m\ge2\), start with \(S_2=S_{\epsilon_1}(U_w)\) and,
for \(j=2,\ldots,m\), use the original ordinary transfer
\[
 \begin{split}
 T_j&=\frac{1-T_{j-1}(1-S_j)^{2+\epsilon_j}/(1-T_{j-1}S_j)}
              {S_j},\\
 S_{j+1}&=\frac{1-S_jT_j}
             {T_j(1-S_jT_j)+(1-T_j)^{2+\epsilon_j}} .
 \end{split}                                                    \tag{9}
\]
The last output \(S_{m+1}\) is \(C\). This defines a rational
function \(\mathcal C_w(U)\) for every finite word.

All these formulas are identities on the root supplied by (2)--(4).
The original regular strips exclude every single or product
exponential equal to one in their denominators. For example the
second denominator in (9) equals \((1-S_jT_j)/S_{j+1}\).
The initializer has the same nonvanishing property by its source
proof. Consequently \(\mathcal C_w\) is holomorphic near every
actual \(U_w(c)\), and
\[
 \mathcal C_w(U_w(c))=C(c),\qquad
 \mathcal C_w'(U_w(c))\,U_w'(c)=-2\pi i C(c)\ne0.               \tag{10}
\]
Thus both derivatives in (10) are nonzero. No converse accepting an
arbitrary rational preimage is used: the selected sheet has already
been defined by the original logarithmic equations. Clearing
denominators or changing their logarithmic lifts would not define
this sheet.

At the last vertex, write \(P=e^{-2\pi i s_m}\) and
\(Q_*=e^{-2\pi i q_w}\). The last equation, including the
final Gram incidence, is
\[
 \begin{split}
 0={}&g'(s_m+q_w)+g'(q_w+c)
                  -(2+\epsilon_m)g'(q_w)+2\pi ic,\\
 (1-PQ_*)(1-Q_*C)&=C(1-Q_*)^{2+\epsilon_m},\\
 C&=\frac{1-PQ_*}
       {Q_*(1-PQ_*)+(1-Q_*)^{2+\epsilon_m}} .
 \end{split}                                                    \tag{11}
\]
It is valid also for \(m=1\). The exponent is \(2+\epsilon_m\);
the coefficient \(2\) belongs to the final Gram incidence, not to
the pre-Gram action.

## 3. Global coordinates, including a uniform last-leg bound

**Theorem 1.** For every nonempty positive \(3/4\) word, both
\(U_w:\Omega\to U_w(\Omega)\) and
\(q_w:\Omega\to q_w(\Omega)\) are one-to-one holomorphic maps
with holomorphic inverses. Their derivatives never vanish.
There are constants \(0<c_q<C_q<\infty\), independent of the
word and its length, such that
\[
                  c_q\le |q_w'(c)|\le C_q
               \qquad(c\in D_3\cup D_4).                     \tag{12}
\]
The derivatives at the closed-disk boundaries refer to the local
holomorphic extensions. No word-independent lower bound on
\(|U_w'|\) is asserted.

*Proof.* Let \(\mathcal H=\mathcal A_{w,zz}''\) at the root,
and let \(\mathcal H_0\) delete its last row and column.
Only the last gradient contains \(c\). With
\[
                  \gamma=G_{qc}(q_w,c)
                         =\frac{2\pi i}{1-Q_*C}\ne0,
                                                               \tag{13}
\]
implicit differentiation and the principal cofactor give
\[
 q_w'(c)=-(\mathcal H^{-1})_{nn}\gamma
        =-\frac{\det\mathcal H_0}{\det\mathcal H}\gamma\ne0,
                  \qquad n=2m+1.                            \tag{14}
\]
Both determinants are nonzero by (4). This argument involves no
conjugation in the implicit derivative.

For the uniform bounds, put \(A=-\mathcal H\). The exact inverse
identity and (4) give
\[
 \Re(A^{-1})=A^{-*}(\Re A)A^{-1}
       \succeq\frac{\mu}{C_H^2}I,\qquad
                    \|A^{-1}\|_2\le\frac1\mu .
                                                               \tag{15}
\]
Indeed \(\|A^{-1}v\|\ge\|v\|/C_H\); applying this to the
quadratic form in (15) proves its lower bound. Thus the modulus
of the final diagonal entry of \(\mathcal H^{-1}\) is at least
\(\mu/C_H^2\).
Both \(q_w,c\) lie in the fixed compact rectangle \(Q\).
Their sum has real part in \([.46,.90]\), so (13) has fixed
positive lower and finite upper modulus bounds
\(0<\gamma_-\le|\gamma|\le\gamma_+\).
Therefore (12) follows with
\[
        c_q=\frac{\mu\gamma_-}{C_H^2},
                      \qquad C_q=\frac{\gamma_+}{\mu}.         \tag{16}
\]

Equation (10) proves \(U_w'\ne0\). If
\(U_w(c_1)=U_w(c_2)\), rational reconstruction gives
\(e^{-2\pi ic_1}=e^{-2\pi ic_2}\). The total real width of
\(\Omega\) is less than one. Hence \(c_1=c_2\).

Suppose instead \(q_w(c_1)=q_w(c_2)=q\). With this exact
complex \(q\) fixed, the other \(2m\) stationary equations do
not contain \(c\). Both internal roots lie in the same convex
product (3). Their Hessian is the corresponding principal block
of (4); integrating along the straight complex segment proves
injectivity of the internal gradient. Explicitly, if \(v\)
is the difference of two roots, the real part of the scalar product
of \(v\) with the negative gradient difference is at least
\(\mu\|v\|^2\). Since the gradient difference is zero, \(v=0\).
The last relation (11) now gives the same \(C\), and hence the
same \(c\). For \(m=1\), these internal variables are just
\((u,s_1)\), so the same argument applies without an ordinary
intermediate vertex.

The nonzero derivatives and global injectivity give holomorphic
inverses on the two images. The actual rational sheet is
\(U_w(\Omega)\), on which (10) and the unique \(c\)-lift recover
the inverse. Nothing asserts global injectivity of
\(\mathcal C_w\) on the entire rational parameter sphere.
\(\square\)

There is also a uniform image-domain consequence. Let
\(K\Subset\Omega\) and choose \(\delta_K>0\) so that every
closed \(D(c,\delta_K)\), \(c\in K\), is contained in
\(\Omega\). The fixed rectangle \(Q\) gives \(|q_w|<1\).
Cauchy's coefficient bound at \(c\) therefore gives, for
\(|v|=r\le\delta_K/2\),
\[
 |q_w(c+v)-q_w(c)-q_w'(c)v|\le\frac{2r^2}{\delta_K^2}.
\]
Choose
\[
 r_K=\min\left\{\frac{\delta_K}{2},
                         \frac{c_q\delta_K^2}{8}\right\}.
\]
The remainder is then at most \(c_qr_K/4\). For every
\(|\eta|<c_qr_K/2\), the linear function
\(q_w'(c)v-\eta\) has modulus greater than \(c_qr_K/2\)
on \(|v|=r_K\) and has one zero inside. Rouché's theorem
gives the same zero count for \(q_w(c+v)-q_w(c)-\eta\).
Consequently
\[
 D\!\left(q_w(c),\,\frac{c_qr_K}{2}\right)
                  \subset q_w(D(c,r_K))\subset q_w(\Omega).
                                                               \tag{16a}
\]
The radius is independent of the word and its length. This is an
image-domain statement for the geometric sheet, not a uniform
finite-source estimate or a claim that a chosen old reference lies
in that image.

## 4. Absolute pre-Gram action and the exact source convention

**Corollary 2.** There is one absolute holomorphic pre-Gram action
on \(q_w(\Omega)\), namely
\[
 \begin{split}
 \mathscr P_w(c)&=H_w(c)-G(q_w(c),c),\\
 \mathcal P_w(q)&=\mathscr P_w(q_w^{-1}(q)),\\
 \mathcal P_w'(q)&=g'(s_m(q)+q)-\epsilon_mg'(q).
 \end{split}                                                    \tag{17}
\]
Here \(q_w^{-1}\) is the inverse of Theorem 1 and \(s_m(q)\)
is the corresponding last incoming leg.

*Proof.* All primitives in (1) have their original constants and
lifts on the common regular domain. Stationary differentiation
gives \(H_w'=G_c\), and therefore
\(\mathscr P_w'=-G_q q_w'\). The last stationary equation
then yields (17). In particular an own-three last vertex gives
\(\mathcal P_w'=g'(s_m+q)\), and an own-four last vertex gives
\(\mathcal P_w'=g'(s_m+q)-g'(q)\). No \(-2g(q)\), terminal
ordinary halfweight, or extra Gram action is inserted.
\(\square\)

The pre-Gram phase also has word-independent derivative bounds.
For \(m=1\), \(s_m\in\mathcal E\); for \(m\ge2\),
\(s_m\in Q\). In both cases \(q\in Q\), and every sum
\(s_m+q\) stays in a fixed compact regular strip with real part
in \([.46,.92]\) and imaginary part in \([-.24,.24]\).
Thus (17) gives a finite constant \(L\), independent of the word,
such that
\[
                |\mathcal P_w'(q)|\le L
                       \qquad(q\in q_w(\Omega)).              \tag{17a}
\]
For \(K\Subset\Omega\), let \(R_K=c_qr_K/2\) be the
uniform image radius in (16a). On the neighborhood
\(\{q:\operatorname{dist}(q,q_w(K))<R_K/4\}\), a disk of
radius \(R_K/2\) about each point lies in \(q_w(\Omega)\).
Cauchy's formula applied to (17a) therefore gives, for every
fixed \(k\ge0\),
\[
       |\mathcal P_w^{(k+1)}(q)|
                  \le k!\,L\left(\frac{2}{R_K}\right)^k .
                                                               \tag{17b}
\]
These are bounds for the derivative and its jets, not for the
absolute value of \(\mathcal P_w\). The latter retains its
word-dependent action constant and can grow with the length.

The convention can also be checked directly against the exact
[mixed Fourier contraction](research_mixed_wire_exact_contraction.md),
equations (10)--(14). Let \(b_N(-2)=S v_N(-2)\),
\(\Gamma=SS^T\), and let \(B_3,B_4\) be its literal block matrices.
The pre-Gram coefficient row and the row after one more incidence are
\[
 \begin{split}
 \rho_{w,N}^{\,T}
   &=b_N(-2)^T B_{3+\epsilon_1}\Gamma B_{3+\epsilon_2}
                  \cdots\Gamma B_{3+\epsilon_m},\\
 d_{w,N}^{\,T}&=\rho_{w,N}^{\,T}\Gamma .
 \end{split}                                                    \tag{18}
\]
There are respectively \(m-1\) and \(m\) Gram matrices; at
\(m=1\) the first row is just \(b_N(-2)^TB_{3+\epsilon_1}\).
The block scalars \(\kappa_N,\kappa_N^2N\), all original
chirps, and any prescribed observation remain as in that exact
identity. Equation (17) removes only the last incidence from the
geometric action \(H_w\); it is not a division by an ordinary
endpoint packet or a scalar renormalization of (18).

Where a separately proved pre-Gram source germ uses the same
original critical point, uniqueness and (1) identify its action
with (17). This does not assert that any previously saved private
reference belongs to \(q_w(\Omega)\). Nor does (17) prove a
whole finite-source packet on that image. It gives a globally
specified action for the actual following-family comparisons.

## 5. A source maximum principle with its missing input explicit

Let \(K\Subset\Omega\) be the closure of a bounded domain, and
suppose an already specified exact finite source
\(\mathfrak F_{w,N}(q)\), with its own stated scalar normalization,
is holomorphic on a neighborhood of \(q_w(K)\). Then
\[
       \mathcal R_{w,N}(c)
          =e^{-N\mathscr P_w(c)}\mathfrak F_{w,N}(q_w(c))
                                                               \tag{19}
\]
is holomorphic near \(K\). If a finite cover of its complete
boundary has uniform bounds
\[
 |\mathcal R_{w,N}(c)|\le A N^r e^{-N\delta},
                    \qquad c\in\partial K,\quad\delta>0,        \tag{20}
\]
the maximum-modulus principle gives the same bound on \(K\).
Different boundary pieces may use different proved majorants;
one takes their common polynomial prefactor and smallest positive
gap in (20). No subharmonicity of the minimum of those majorants
is required. Bounds on a fixed enlarged domain also give all fixed
normalized \(c\)-derivative bounds on a smaller domain by Cauchy's
formula.

For example the four compact clipped following domains
\(O_3,O_4,A_3,A_4\) of
[actual last-row references](research_mixed_actual_last_row_reference_domains.md)
are admissible \(K\)'s. This supplies the same boundary-reduction
geometry for every word. It supplies neither the source hypothesis
nor the positive boundary gaps for an unestimated word. Canonical
finite interpolation, if used to define a source, must still retain
its original observations and ordinary normal adapters. No assertion
about arbitrary closing, mixed signs, branching, or a new knot
family follows from this geometric theorem.
