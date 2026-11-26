# The actual prepared three-four cap: source and main domain

Research deduction, 7 November 2026. Replacing the incoming Fourier
vector of the completed three-four kernel by the original ordinary
cap changes the phase by an amount proportional to \(N\). The result
has an exact three-index representation which keeps the first cap
coherent, and an expanded four-index representation on which the
existing cap curvature proves strict accretivity. These are source
and domain statements, not a prepared-cap asymptotic at the
alternating output. No numerical evaluation is used.

## 1. The function not yet supplied by the existing source theorems

Keep the original matrices, ordinary vector and half-band cardinal
vector, and put
\[
 G_{34,N}(y,w)=v_N(w)^T A_{3,N}A_{4,N}h_N(y),\qquad
 Y=e^{2\pi iy}.
 \tag{1}
\]
The intended output is a fixed neighborhood of the original alternating
parameter \(x_0=x_{34}\), not a retained-leg coordinate.
The [whole paired-kernel theorem](research_mixed_contracted_pair_full_kernel.md)
proves the source asymptotic for \(h_N(x)^TA_3A_4h_N(y)\)
near \((x_0,x_0)\). Its first boundary vector is different
from that in (1).

The [homogeneous prepared-source theorem](research_three_full_boundary_source_propagation.md)
instead concerns \(v(w)^TA_3^m h(y)\), on its stated local
domain about \(x_h=1/6+i\log2/(2\pi)\). The
[exact Fourier-message bridge](research_mixed_conditional_fourier_message_bridge.md),
Section 3, records \(|x_0-x_h|>.035\) and does not extend
that domain or permit a type-four attachment. Finally, the
[alternating cap entrance theorem](research_mixed_alternating_cap_phase_entrance.md)
constructs an original local phase for sufficiently long alternating
prefixes. Its eventual entrance assertion does not include the specific
two-letter prefix (1), or a whole-message remainder bound for it.

Thus none of these results asserts a nonzero asymptotic for (1) near
\((y,w)=(x_0,-2)\). The following identities specify that
actual source without substituting an arbitrary input envelope.

## 2. Exact four- and three-index representations

Set
\[
 r=e^{-2\pi i/N},\quad Q=r^{-1},\quad P_j=(r;r)_j,
 \quad \kappa=e^{\pi i(N-1)^2/(2N)},\quad
 c_y=\frac{e^{-\pi i(N-1)y}(1-Y^N)}N.
 \tag{2}
\]
Use the literal complete Newton polynomial
\(\mathcal H_N(w,Z)\) and first cap \(U_{0,N}(w,Z)\)
from [conditional torus composition](research_mixed_conditional_torus_composition.md),
equation (21). In the common finite basis of
[exact wire contraction](research_mixed_wire_exact_contraction.md),
\[
 b_i(w)=(Sv(w))_i=\frac{\mathcal H_N(w,r^{-i})}{P_i},
 \qquad f_l(y)=\frac{c_yY^l}{(Y;r)_{l+1}}.
 \tag{3}
\]
The second quotient has its original removable continuation. In a
fixed neighborhood of \(x_0\), \(0<|Y|<1\), so its displayed
denominator is nonzero.

**Proposition 1.** The whole function (1) is exactly
\[
 \begin{split}
 G_{34,N}(y,w)=\kappa^3Nc_y
 \sum_{\substack{i,j,k,l\ge0\\i+j<N,\ j+k<N,\ k+l<N}}
 \frac{\mathcal H_N(w,r^{-i})Y^l Q^{jk}
            P_{i+j}P_{j+k}P_{k+l}}
 {P_iP_j^2P_k^3P_l(Y;r)_{l+1}}.
 \end{split}
 \tag{4}
\]
Equivalently, after summing the first private index coherently,
\[
 G_{34,N}(y,w)=\kappa^3Nc_y
 \sum_{\substack{j,k,l\ge0\\j+k<N,\ k+l<N}}
 \frac{U_{0,N}(w,r^j)Y^lQ^{jk}P_{j+k}P_{k+l}}
 {P_jP_k^3P_l(Y;r)_{l+1}}.
 \tag{5}
\]
Both identities retain all ordinary derivatives and both level parities.

*Proof.* The original matrix identity is
\(G_{34,N}=b(w)^TB_3\Gamma B_4f(y)\).
Insert the three matrices from equations (5) and (10) of exact wire
contraction and (3). Their scalar is precisely \(\kappa^3N\),
and their three triangular zeros give the support in (4). At a physical
node,
\[
 P_jU_{0,N}(w,r^j)
   =\sum_{i+j<N}\frac{\mathcal H_N(w,r^{-i})P_{i+j}}{P_i},
 \tag{6}
\]
because \((r^{j+1};r)_i=P_{i+j}/P_j\) on that support
and vanishes outside it. Substituting (6) gives (5). All sums are
finite. \(\square\)

In the exact notation of the Fourier-message bridge these formulas read
\[
              G_{34,N}=\kappa^3N\,\mathcal E_1
                               \mathcal T_{01}U_{0,N}.
 \tag{7}
\]
This confirms both the power of \(N\) and the output flag.
Here \(\mathcal T_{01}\) has input flag zero, so its
constant-term identity contains no retained type-four weight. Type four
is the output flag of \(\mathcal E_1\), already represented
by the displayed factorial powers and scalar. Equations (5)--(7)
perform the complete physical-node contraction; no extra selection
factor or selected monomial may be added to (5).

## 3. The original endpoint replaces the first external incidence

Write \(s=i/N,t=j/N,p=k/N,q=l/N\). Their closed supported
physical domain is the same polytope as for the paired kernel:
\[
 \Omega=\{s,t,p,q\ge0:s+t\le1,\ t+p\le1,\ p+q\le1\}.
 \tag{8}
\]
The endpoint factor in (3) has the specified holomorphic interpolation
\[
 b_N(s,w)=D_N(s)^{-1}C_N(s,w),\qquad
 D_N(s)=\exp\!\left(\frac{\pi i}{2}[N(s-s^2)-s]\right).
 \tag{9}
\]
It agrees with every physical coefficient \(b_i(w)\), and
\(C_N\) is the full finite sum of
[complex-index continuation](research_complete_boundary_complex_index.md).
Its Section 6, equation (18), proves the exact identity
\(G_N(Ns)C_N(s,w)=\mathcal H_N(w,e^{2\pi is})\).
Thus (9) is also the literal polynomial divided by its marked
factorial \(D_N(s)G_N(Ns)\); the off-grid identification is
not inferred merely from agreement at finitely many nodes.
The [endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md)
gives \(C_N=N^{-3/2}\mathcal A(s,w)e^{NS(s,w)}(1+O(N^{-1}))\)
on a neighborhood of
\(E_c=[.27,.49]+i[-.055,.04]\), with \(\mathcal A\ne0\).
In particular the Newton terms revived off the physical grid remain
inside this interpolant.

Keep the original primitives
\[
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\quad J(0)=0,\qquad
 \ell_q(y)=2\pi iqy-I_Y(q)-\pi iy,
 \quad I_Y(q)=\frac{\operatorname{Li}_2(Ye^{-2\pi iq})-
                                \operatorname{Li}_2(Y)}{2\pi i}.
 \tag{10}
\]
The complete main phase of (4) is
\[
 \begin{split}
 \mathcal F_{\mathrm{cap}}(s,t,p,q;y,w)={}&
 S(s,w)-\frac{\pi i}{2}(s-s^2)
 +g(s+t)+g(t+p)+g(p+q)\\
 &-2g(t)-3g(p)-g(q)+2\pi itp+\ell_q(y).
 \end{split}
 \tag{11}
\]
No additive constant has been chosen anew. In particular, compared with
the original paired phase at first Fourier input \(x_0\),
\[
 \mathcal F_{\mathrm{cap}}-
                  \mathcal F_{34}(s,t,p,q;x_0,y)
   = S(s,w)-\frac{\pi i}{2}(s-s^2)-\ell_s(x_0).
 \tag{12}
\]
This is an order-one action difference multiplied by \(N\) in
the source. It cannot be absorbed into a bounded amplitude. Neither
the paired critical point nor its action and tail margins transfer
through (12).

If the private first index is eliminated on its original stationary
branch, (11) becomes the three-index phase
\[
 \mathcal T_0(t,w)+g(t+p)+g(p+q)-g(t)-3g(p)-g(q)
                                      +2\pi itp+\ell_q(y).
 \tag{13}
\]
This interpretation uses the actual \(U_0\) packet only where its
stated attached-leg domain holds. Formula (5) itself has no such domain
restriction and includes every physical value of \(t\).

## 4. A proved main rectangle for the new phase

Put
\[
 T=[.22,.5]+i[-.03,.015],\quad
 R=[.2,.42]+i[-.055,.015],\qquad
 \mathscr R_{\mathrm{cap}}=E_c\times T\times R^2.
 \tag{14}
\]
All three factorial sum arguments in (11) are strictly inside the
original regular strip: their real parts lie in
\([.49,.99],[.42,.92],[.4,.84]\), respectively.
The external denominator is regular by the original
\(|e^{2\pi ix_0}|e^{.03\pi}<.7\).

**Proposition 2.** There are a fixed neighborhood of
\((y,w)=(x_0,-2)\) and \(\mu>0\) such that
\[
          -\Re\mathcal F_{\mathrm{cap}}''\succeq\mu I_4
                \quad\hbox{throughout }\mathscr R_{\mathrm{cap}}.
 \tag{15}
\]
The Hessian is in \((s,t,p,q)\). Hence there is at most one
critical point in this convex rectangle; any such point is
nondegenerate. This does not assert existence or identify its branch.

*Proof.* Set \(V(z,z')=g(z+z')-g(z)-g(z')\). The exact
decomposition at complete ordinary color is
\[
 \mathcal F_{\mathrm{cap}}
   =\Psi_0(s,t)+V(t,p)+V(p,q)-g(p)+2\pi itp+\ell_q(y),
 \qquad \Psi_0=S(s)+J(s+t)-J(t)-\pi ist.
 \tag{16}
\]
Lemma 1 of [the upper-target cap domain](research_mixed_cap_upper_target_extension.md)
gives \(-\Re\Psi_0''\succ(\pi/200)I_2\) on the larger
product \(E_c\times([.22,.5]+i[-.108,.021])\).

For \(t\in T\), \(|\Im\cot\pi t|<1\): its equivalent
inequality is \(\cos(2\pi\Re t)<e^{-2\pi|\Im t|}\),
and the left side is less than \(1/5\), while the right side
exceeds \(1/2\). For \(p,q\in R\), the same inequality is
proved in the contracted-pair rectangle theorem. The original complex
triangle criterion therefore makes \(-\Re V(t,p)''\) and
\(-\Re V(p,q)''\) positive semidefinite, and the latter is
positive definite. The endpoint \(\Re t=1/2\) follows by
continuity; the cap form remains strictly positive there.
The term \(-g(p)\) adds a nonnegative diagonal form, and the
chirp has zero real Hessian. Finally
\[
 -\Re\ell_{q,qq}(x_0)
 =\frac{-2\pi\Im(Ye^{-2\pi iq})}{|1-Ye^{-2\pi iq}|^2}>0
                \quad(Y=e^{2\pi ix_0}),
 \tag{17}
\]
since \(-1/2<\Re x_0-\Re q<0\). The cap form covers
\((s,t)\), and the second triangle covers \((p,q)\).
Their sum is strictly positive on the whole compact product.
Compactness and continuity give (15) and its fixed parameter
neighborhood. Strict accretivity along a straight complex segment
proves uniqueness, and gives invertibility at any zero.
\(\square\)

For normalization, put
\(a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}\) on the
original branches. The retained row in (4) has the expansion
\[
 \kappa^3N^{-3}b_{\mathrm{cap}}e^{N\mathcal F_{\mathrm{cap}}}
                  (1+O(N^{-1})),\qquad
 b_{\mathrm{cap}}=
 \frac{e^{i\pi s/2+\pi iy}\mathcal A(s,w)
            a(s+t)a(t+p)a(p+q)}
 {a(t)^2a(p)^3a(q)\sqrt{(1-Y)(1-Ye^{-2\pi iq})}}.
 \tag{18}
\]
Every factor is nonzero. If a critical point is established strictly
inside this product, its own local four-dimensional current has power
\(N^4N^{-3}N^{-2}=N^{-1}\), amplitude
\((2\pi)^2b_{\mathrm{cap}}/\sqrt{\det(-\mathcal F_{\mathrm{cap}}'')}\),
and carrier \(\kappa^3\). This is a local-current statement;
it does not identify it with the complete function (1).

## 5. The precise remaining source comparisons

The first missing datum is an original critical point for (11) at
\(y=x_0,w=-2\), inside (14), with the original logarithmic
lifts. Proposition 2 supplies uniqueness and continuation if existence
is proved; a long-prefix entrance theorem cannot replace this datum
for the particular length two.

Even with that point, the complete physical tail is new. For example,
a literal zero-safe upper bound for the original boundary coefficient
is
\[
 \mathfrak B(s)=\max_{0\le u\le s}
      \{\mathcal V(u)-J(u)-J(s-u)\},\qquad
 \mathcal V(u)=2\int_0^u\log(2|\cos\pi v|)\,dv-2J(u).
 \tag{19}
\]
This follows from the physical finite coefficient formula in the
complex-index theorem, retaining all its terms and fixed ordinary jets.
Uniform sine-factorial bounds and at most \(N\) summands cost only
a power of \(N\). Thus the supported physical rows in (4) have
the upper rate
\[
 \begin{split}
 E_{\mathrm{cap}}={}&\mathfrak B(s)+J(s+t)+J(t+p)+J(p+q)
                  -2J(t)-3J(p)-J(q)\\
 &-\tfrac12\log|Y|+q\log|Y|
             -\int_0^q\log|1-Ye^{-2\pi iv}|\,dv.
 \end{split}
 \tag{20}
\]
It extends continuously to the closed physical polytope. Exact
sum-\(N\) rows remain zero. No claim is made that this absolute
upper rate is sharp enough. In particular (20) differs from the
completed paired-tail rate by replacing its incoming cardinal
incidence by \(\mathfrak B(s)\). The old nine-face values
cannot certify this new comparison.

The alternative (5) retains cancellation in the complete first cap
before any modulus. It requires its actual source bounds for every
retained physical \(t\), and subsequent contour bounds where the
three-index source is deformed. Existing first-cap bounds on original
attached heights do not automatically cover these independent moving
parameters. This is the precise place where the coherent option can
improve on (19), without pretending that the needed inequality is
already proved.

On the retained four-index box the exact lattice formula also has all
joining and alias currents. The new private range is
\([.27,.49]+i[-.055,.04]\); it is not the old first Fourier
index rectangle. The coefficient \(C_N(s,w)\) already controls
its own internal Newton tails there, but the four outer index currents
still require comparisons for (11). Neither the old eight paired
alias margins nor its \(\pm2\pi\) gradient strips may be
copied through (12). A strict new physical and current gap, together
with an identified interior critical point, would turn the local
coefficient in (18) into a nonzero whole prepared cap.

Finally, a whole prepared-cap theorem only near \(x_0\) would
still leave its full outgoing-period envelope and propagated
remainder to be proved before iterating the full paired operator.
This note supplies the exact finite source and a genuinely shared
main curvature domain for that first preparation problem. It supplies
no whole mixed-word source estimate, knot identity, or short-filling
stability theorem.
