# The second-selected first-three product on the incoming right segment

Research deduction, 7 November 2026. The already calibrated second-selected
product extends from its first incoming plateau to the horizontal segment
from \(9/20\) to \(1/2\), at the original incoming height. This uses the
same ordinary-next canonical references as the completed plateau theorem.
It does not replace an ordinary next vertex by a terminal reference, and
does not estimate the entire selected Fourier coefficient.

No new numerical evaluation or saved comparison is used. The earlier
central and half-row scalar certificates are reused only after proving
that their identical scalar majorants bound the enlarged target domain.

## 1. The exact product and reference family

Use the canonical reference and notation of
[the first-three second-selected plateau theorem](research_mixed_second_selected_first_three_plateau_completion.md):
\[
 r=(a_*,u_*,z_*,v_*,b_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
 \qquad (\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),
 \quad \beta\in\{0,1\}.                                      \tag{1}
\]
Both \(u_*,v_*\) are ordinary indices. The next external parameter is
the same \(c=s_4^*\in K_3\cup K_4\) as in that theorem, including its
canonical parameters not known to be realized by a suffix. Put
\[
 P=[11/50,9/20],\quad H=1/100,\quad
 a=x+ih_a,\ z=y+iH,\ b=w+ih_b,
 \quad x\in[9/20,1/2],\quad y,w\in P,                         \tag{2}
\]
where \(h_a=\Im a_*,h_u=\Im u_*,h_b=\Im b_*\).
The original bare phases, allocated reference, and marginals are
\[
 \begin{split}
 Q_\epsilon(t;a,b)&=g(t+a)+g(t+b)-(2+\epsilon)g(t)
                           -g(a)-g(b)+2\pi iat,\\
 F_*&=Q_1(u_*;a_*,z_*)+Q_\beta(v_*;z_*,b_*)
                                      -g(z_*)-\tfrac\beta2g(b_*),\\
 p_L&=g'(a_*+u_*)-g'(a_*)+2\pi iu_*,\\
 p_R&=g'(v_*+b_*)-(1+\beta/2)g'(b_*),\\
 \Lambda_{23}(a,b)&=\Re F_*+
                    \Re\{p_L(a-a_*)+p_R(b-b_*)\}.
 \end{split}                                                   \tag{3}
\]
All lifts and additive constants are unchanged. Let \(T_0\) be the
original first-cap action, \(A=\Re a_*\), and 
\[
 \Lambda_{123}(b)=\Re\{T_0(a_*)+F_*\}
                            +\Re\{p_R(b-b_*)\}.               \tag{4}
\]
The original attached equation is \(T_0'(a_*)+p_L=0\).

Write \(X=e^{-2\pi ia},Y=e^{-2\pi iz},Z=e^{-2\pi ib}\). The
literal nonnegative product considered here is
\[
 \mathcal B_N=
 |U_{0,N}(\omega,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)d_N(Y)Y^{-N}|
                                      |d_N(Z)|^{\beta/2}.       \tag{5}
\]
There is no incoming Fourier halfweight. At \(\beta=0\) the last
factor equals one even at a zero of \(d_N\).

**Theorem.** For every prescribed \(\tau>0\), the complete product (5)
satisfies
\[
 \mathcal B_N\le C_\tau N^{B_\tau}
       \exp N\{\Lambda_{123}(b)-1/400+\tau\}                  \tag{6}
\]
at complete ordinary color \(\omega=-2\), uniformly on (1)--(2),
for both parities and all sufficiently large levels. The same rate
holds for all real ordinary colors and fixed ordinary-color derivatives,
with their polynomial factors, and on a sufficiently small fixed
complete-color neighborhood with its prescribed additional tolerance.
Thus a finite rate loss \(1/800\) is available after choosing the total
tolerance and absorbing polynomial factors. All rows of both conditional
polynomials, both Fourier alternatives, and all currents are retained.

An unchanged ordinary suffix can be joined with the original outgoing
halfweight and marginal. This pays this particular incoming-right
piece of the second-selected source; it does not pay the other pieces
of either retained-variable contour.

## 2. A negative incoming height and the enlarged central budget

The original reference identification is essential. The first two
vertices in (1) are precisely the half-chain (34) with external
coordinate \(v_*\in O_{3+\beta}\subset P_{3+\beta}\). Uniqueness of the
original-log half-chain therefore identifies its first attached
coordinate with \(a_*\). The full-disk geometric guards in
[the following connector theorem](research_mixed_three_four_following_connector_gap.md)
give
\[
                         h_a<0.                              \tag{7}
\]
This applies to the entire canonical family (1), since its ordinary
image theorem places \(v_*\) in that same typed set. It is not an
inference from independent containing boxes. The unchanged bounds are
\[
 -.072<h_a<0,\qquad -.102<h_u<-.001,
 \qquad .24<\Re u_*<.36 .                                    \tag{8}
\]

First extend the original \(u>11/50\) maximizing barrier. Only
\(x\ge9/20\) is new. For \(1/8\le t\le11/50\), put

\[
 r=e^{2\pi h_u}\in(1/2,1),\quad T=e^{-2\pi h_a}\ge1,
 \quad R=e^{2\pi H}>1,\quad D=1+r^2-9r/25 .                  \tag{9}
\]
Including the incoming chirp, the exact squared force is
\[
 e^{2\Re Q_{1,t}(t+ih_u;a,z)}
 =\frac{|T-r e^{-2\pi i(x+t)}|^2
             |1-Rr e^{-2\pi i(y+t)}|^2}
            {|1-r e^{-2\pi it}|^6}.                         \tag{10}
\]
Here \(x+t\in[.575,.72]\), so its cosine is negative;

\(y+t\in[.345,.67]\), so its cosine is less than \(-12/25\);
and \(\cos(2\pi t)>9/50\). The last two elementary bounds are the
same guards proved in
[the original index-barrier theorem](research_mixed_second_selected_horizontal_concavity.md).
Consequently the two numerator squares exceed \(D+9r/25\) and

\(D+33r/25\). Since
\[
 D\le41/25,\qquad D/r=r+r^{-1}-9/25\le107/50<5/2,
\]
equation (10) is strictly greater than
\[
 \frac{(1+(9/25)(2/5))(1+(33/25)(2/5))}{41/25}
                      =\frac{27313}{25625}>1.               \tag{11}
\]
The force is therefore positive throughout this entire smaller-index
interval, for either Fourier alternative and either right profile.

For \(t\in[.22,.5]\), the only new pair in the central Hessian is

\(V(u,a)=g(u+a)-g(u)-g(a)\) with \(a_R\in[.45,.5]\).
Writing \(C(w)=\Re\cot\pi w\), its exact negative real Hessian is
\[
 -\pi^{-1}\Re V''=
 \operatorname{diag}(C(u),C(a))-C(u+a)
                          \begin{pmatrix}1&1\\1&1\end{pmatrix}.
                                                                  \tag{12}
\]
The first two entries are nonnegative and \(C(u+a)\le0\), because

\(.67\le\Re(u+a)\le1\). Thus (12) is at least

\(\operatorname{diag}(0,C(a)/2)\), exactly the incoming pair cost
used in the old directional and half-row budgets. At the upper corner
the summed height is strictly negative by (8), so the original lower
continuation is regular; the displayed real Hessian has its continuous
limit there. All other pair bounds and all downward right-index
curvature gains are unchanged.

At the vertically shifted original real reference, the incoming force
is still zero: \(Q_{1,a}\) depends on \(a,u\), not on \(z\). Therefore
[the directional majorant](research_mixed_second_selected_directional_budget.md),
(15)--(18), holds verbatim on the enlarged product with

\(a_R\in[.22,.5]\). Its discarded incoming cost is nonnegative on
every connecting segment by (12). Its three scalar gains, reference
forces, selected intervals, and all guarded one-variable improvements
are literally unchanged. The same argument applies to
[the half-row budget](research_mixed_second_selected_half_row_budget.md),
whose incoming force also vanishes and whose incoming cost was likewise
discarded.

This explains precisely why the completed scalar certificates apply
without a new calculation. Their boundary majorants contain no incoming
target coordinate or incoming optimization. The whole-boundary response

\(|p_L'a_*'|+|p_R'b_*'|\) is a property of the unchanged reference.
The target Hessian is still nonpositive on the enlarged product, so
the same stationary-reference Laplacian identity and disk barrier give
the same interior losses. Hence
[the central completion](research_mixed_second_selected_first_three_central_completion.md)
retains its gaps \(1/100\) for \(\beta=0\), \(1/200\) for

\(\beta=1\), while
[the first-three half-row completion](research_mixed_second_selected_first_three_half_row_completion.md)
retains its gap \(1/20\). The outgoing-four half-row and left-cut
comparisons involve no \(a\) and are unchanged. These statements retain
both complete Fourier alternatives.

## 3. Two non-main profiles of the first conditional factor

Keep the old trial \(s_h=3/10+ih_u\). The completed pointwise comparisons
on the old plateau are \(R_R^2<R_0^2-1/30\) and

\(R_1^2<R_0^2-1/50\), with their precise containing height domains,
as recorded in
[the four-profile reduction](research_mixed_second_selected_four_profile_reduction.md).

For the half row, the difference

\(\Delta(x)=\Re[Q_1(s_h;x+ih_a,z)-Q_1(1/2;x+ih_a,z)]\)
has derivative
\[
 \Delta'(x)=\log\left|\frac{S^{-1}-X}{1+X}\right|,
 \qquad S=e^{-2\pi is_h}.                                  \tag{13}
\]
On \(x\in[.45,.5]\), with \(q=|S|^{-1}<2\) and \(\rho=|X|\),
the difference of its squared numerator and denominator is
\[
 q^2-1-2\rho\{q\cos(2\pi(x+.3))+\cos(2\pi x)\}>0.          \tag{14}
\]
Indeed the braces are less than \(2/3-9/10<0\):

\(\cos(2\pi(x+.3))\le\cos(8\pi/5)=(\sqrt5-1)/4<1/3\),
and \(\cos(2\pi x)\le-\cos(\pi/10)<-9/10\).
The old half-row reserve therefore persists throughout the right segment.

For the last row, put
\[
 K(x)=\Re\{g(x+ih_a+s_h)-g(x+ih_a)+2\pi i(x+ih_a)s_h\},
 \qquad f_\rho(t)=\log|1-\rho e^{-2\pi it}|,
 \quad 0<\rho=e^{2\pi h_a}\le1.                            \tag{15}
\]
The exact chirp-aware derivative and \(q\ge1\) give
\[
 K'(x)=\log|q-\rho e^{-2\pi i(x+.3)}|-f_\rho(x)
                 \ge f_\rho(x+.3)-f_\rho(x).                \tag{16}
\]
The modulus increases in \(q\ge1\), since \(q-\rho\cos\theta\ge0\).
Reflection \(f_\rho(1-t)=f_\rho(t)\) consequently yields
\[
 K(.5)-K(.22)\ge
       \int_{.2}^{.22}f_\rho(t)\,dt
          -\int_{.48}^{.5}f_\rho(t)\,dt>-\frac3{200}.        \tag{17}
\]
For the last strict inequality, on the first interval

\(|1-\rho e^{-2\pi it}|\ge\sin(2\pi t)\ge\sin(2\pi/5)>19/20\),
whereas on the second it is at most two. Thus the loss is smaller
than \(\log(40/19)/50<3/200\). The sine bound is the exact pentagon
bound already proved in the directional theorem; the logarithm follows
from the first five positive terms of \(e^{3/4}>40/19\).

Furthermore \(K''=\pi[C(a+s_h)-C(a)]<0\) on \([.22,.5]\),
since \(\Re(a+s_h)\in[.52,.8]\). Its minimum on that interval
is at an endpoint. The last-row rate

\(R_1^2=2\pi(-h_a)_++2\pi H\) has no \(x\)-dependence.
The old trial comparison at \(x=.22\), which is uniform in \(y,h_a,h_u\),
and (17) therefore prove
\[
              R_1^2<R_0^2-\frac1{200}
                  \qquad (.22\le x\le.5).                 \tag{18}
\]
This is a new pointwise comparison of original profiles, not an estimate
obtained by dividing or subtracting bounds for signed sums.

## 4. The outgoing last-row profile

The last-row argument on the *second* conditional factor also extends.
First take \(z=y+i\Im z_*\) at its unselected height. The original
allocated \(Q_1-g(z)/2\) supporting plane extends in \(a_R\) through

\(.5\), with all \(u_R\in[1/8,.5]\) and \(y\in P\).
Here is the needed curvature check, before applying any source bound.
For \(u_R\ge.15\), the old pair \(V(u,z)\) has positive negative-real
Hessian, while (12) is positive semidefinite for

\(a_R\ge.45\); the extra \(-g(u)-g(z)/2\) contributes nonnegative
diagonal entries. For \(1/8\le u_R\le.15\), use the exact Schur
calculation in
[the smaller-cut theorem](research_mixed_four_left_cut_extension.md).
Its incoming shifted cotangent is now nonpositive, so its index Schur
debit is nonpositive. The outgoing debit is at most \(187/120\),
whereas the own index diagonal exceeds \(3(21/20)\). This is strictly
positive. The limiting \(a_R=.5\) case follows by continuity.

The path from the actual reference first lies in the old jointly
concave product, and thereafter in this enlarged one. Integrating its
Hessian gives the original affine plane; only an unnecessary quadratic
remainder is dropped. Combining with the unchanged pointwise last-row
plane of factor 3 therefore gives the analogue of (6) in
[the outgoing-last-row theorem](research_mixed_second_selected_outgoing_last_rows.md),
with no quadratic remainder required.

Now move only \(z\) from its actual negative height to \(H\). All
derivatives and estimates (10)--(25) of that theorem involve only the
index of factor 2 and \(z\); they are independent of the incoming real
target \(x\). Their exact last-row change and both Fourier alternatives
therefore retain the same strict deficit \(1/400\). In particular every
term with first main profile and second last-row profile is paid on
the enlarged incoming interval. No signed conditional bound has been
used to infer an individual current bound.

## 5. The moving left cut and the full first conditional contour

Use the moving real cut and fixed main height
\[
 \ell(x)=23/40-x\in[3/40,1/8],\qquad \Im t=h_u .             \tag{19}
\]
The whole-cap plane on the right segment is
\[
 B_U(x)=\Re T_0(a_*)-\Re p_L(x-A)-\kappa_*(x-A)^2,
 \qquad \kappa_*=1/2500000.                                \tag{20}
\]
It follows from
[complete upper-target cap support](research_mixed_cap_upper_target_completion.md)
for the actual own-three, following-four input. It bounds the whole cap,
including its private currents, physical tails, and true ends.

The real part of its marginal satisfies \(\Re T_0'(a_*)<1\), by
the elementary bound (12) in
[the following right-segment theorem](research_mixed_three_four_following_right_segment.md).
Thus \(B_U'(x)<1\). On the moving real cut the exact derivative is
\[
 \frac d{dx}\{B_U(x)+\Re Q_1(\ell(x);x+ih_a,z)\}
 =B_U'(x)+3\log(2\sin\pi\ell(x))
 -\log|e^{-2\pi h_a}-e^{-2\pi ix}|
 -\log|1-e^{-2\pi i(z+\ell(x))}|<-\frac1{10}.              \tag{21}
\]
Indeed \(2\sin\pi\ell<4/5\), the first modulus exceeds \(9/5\)
using \(h_a\le0\) and \(-\cos2\pi x>19/20\), and the second
exceeds one because its radius is greater than one and its real argument
lies in \([.295,.575]\). Use

\(3\log(4/5)<-3/5\) and \(\log(9/5)>1/2\).

At \(x=.45\), every first-left-cut/second-profile combination, including
each Fourier alternative, is already paid with raw loss \(1/400\) by the
pointwise proof of the completed plateau theorem. The cap plane cancels

\(p_L\) there. All other factors in each such combination are independent
of \(x\). Hence (21) transports that very same comparison, with the
same fixed right marginal (4), over the whole interval. This step uses
the profile comparisons that prove the plateau theorem, not an attempted
decomposition of its signed finite-kernel modulus bound.

The added main interval \(\ell(x)\le t\le1/8\) is paid by its right
endpoint. Formula (10), with \(t\) in this smaller interval, has both
numerator moduli greater than one: \(x+t\in[.575,.625]\) and

\(y+t\in[.295,.575]\). Its denominator square is at most \(3/5\),
because \(r\in[1/2,1]\) and \(\cos2\pi t\ge\sqrt2/2>7/10\).
Thus \(\Re Q_{1,t}>0\). Every lower physical row is also included:
at real \(0<t\le\ell(x)\), the incoming modulus exceeds one, the
outgoing modulus exceeds \(9/10\), and the own denominator is less
than \((4/5)^3\). Its real-row rate strictly increases to the paid
cut and extends continuously to the exact row \(j=0\).

Keep the original horizontal aliases at heights \(-1/5\) and \(5/4\).
The original logarithmic argument bounds give, for every finite index
height and \(\ell(x)\le t_R\le.5\),
\[
              -7\pi/4<\Im Q_{1,t}<141\pi/100 .             \tag{22}
\]
To verify both constants directly, divide by \(\pi\). The lower bound
is bounded below by

\(-2+4t_R+\min(0,1-2y-2t_R)\), whose two cases have minima

\(-17/10\) and \(-7/4\). The upper bound is at most

\(2x+\max(0,1-2y-2t_R)\le141/100\). These use
\(a_R+t_R\ge23/40\), so its argument is nonpositive.
The resulting lower and upper weighted horizontal losses relative to
the main line are at least
\[
 \frac{2\pi}{5}-\frac{141\pi}{100}\frac15
       =\frac{59\pi}{500},\qquad
 \frac{5\pi}{2}-\frac{7\pi}{4}\left(\frac54+\frac{51}{500}\right)
       =\frac{67\pi}{500}.                                 \tag{23}
\]
The same argument bounds make the weighted vertical profiles monotone
toward height zero. The unweighted joins from height zero to \(h_u\)
are convex at both real cuts. At the left cut,

\(C(a+t)<0\), \(C(z+t)<1\), and

\(C(t)>(9/20)/(5/4-7/10)=9/11\), so \(\Re Q_{1,tt}<0\).
At the half cut both shifted cotangents are nonpositive and \(C(t)=0\).
If a vertical segment meets \(a+t=1\), the original limiting real phase

\(\Re g(1+i\eta)=\pi\max(\eta,0)\) has an upward derivative jump;
this preserves the claimed height convexity.

The exact interpolant and cuts are
\[
 \mathcal T_N(t;a,z)=e^{2\pi iNat}
      \frac{\Pi_N(a+t)\Pi_N(z+t)}{\Pi_N(a)\Pi_N(z)\Pi_N(t)^3},
 \quad L_N=\lceil N\ell(x)\rceil,\ M_N=\lceil N/2\rceil,
 \quad t_-=(L_N-1/2)/N,\ t_+=(M_N-1/2)/N .                  \tag{24}
\]
At \(t=j/N\) this is exactly \(X^{-j}p_j(X)p_j(Y)/P_j^3\).
Apply the unchanged finite rectangle identity only to

\(L_N\le j<M_N\): its main, two horizontal aliases, four vertical
aliases, and two zero-mode joins remain. All reciprocal arguments are
regular; the possible numerator wall at \(a+t=1\) uses the existing
zero-safe continuation, not a zero-free packet across that wall.
The physical pieces \(j<L_N\) and \(j\ge M_N\) remain literal products.

For the latter piece, Lemma 1 of
[the enlarged high-row endpoint theorem](research_mixed_transformed_upper_rows.md)
applies on \(a_R,z_R\in[.22,.5]\) at the present heights of modulus
at most .108. It reduces the entire absolute high-row sum to the half
and last rates, not to a physical triangle. Those two rates are paid by
(13)--(18) and the extended main comparison. Positive selected height
does not delete any revived row. Uniform product bounds retain all zeros
and the \(O(\log N)\) denominator error. Half-grid shifts are absorbed
into an arbitrarily small total rate tolerance by continuous upper rates.
This preserves the even half row and the odd first row above one half.

## 6. Assembly and remaining scope

On the enlarged main domain, Section 2 pays the two central alternatives
and, when \(\beta=0\), the two outgoing half-row alternatives with their
original gaps. For \(\beta=1\), its unchanged outgoing half-row comparison
reduces them to the central ones. The outgoing left profiles still reduce
to their main profiles. Section 4 pays the outgoing last profile with
loss \(1/400\). Section 3 reduces the first half and last profiles to
its main profile, while Section 5 pays the first moving real cut and all
other first-factor currents. Every resulting combination has raw loss at
least \(1/400\) after multiplication by the whole cap and cancellation
of its original incoming tangent. This proves (6).

Both rates of \(d_N(Y)Y^{-N}\) remain the additive estimates

\(-\Re g(z)-2\pi H\) and zero. The outgoing factor in (5) remains
its original modulus halfweight; it is never divided out. The second
conditional factor keeps the whole original finite-current estimate.
Only finitely many source groups occur. Their polynomial costs and one
prescribed total tolerance give the stated finite loss at both parities.

The complete cap plane has its established all-real ordinary-color bound.
Its coefficientwise source theorem and whole-interval Markov bound give
fixed ordinary derivatives before the strict reserve is spent. On small
complex complete-color neighborhoods, its original holomorphic extension
incurs arbitrarily small rate cost. All fixed derivatives of the literal
integer-weighted source follow by Cauchy on smaller neighborhoods; no
modulus halfweight is differentiated.

At the original outgoing reference \(b=b_*\), a known nonzero negative-
height Fourier halfweight may be removed if desired, with its exact
factorial rate and symbol; this does not change the proof above. Such a
removal is not performed in (5)--(6). In a full ordinary word the other
incidence supplies the missing half and cancels \(p_R\), exactly as in
the plateau assembly. Actual terminal-next graphs, the selected retained
coordinate outside its plateau, the first incoming left/complementary
pieces, and the full coefficient \(N[Y^N](F_{34}d_NC_\beta)\) still require
their own source estimates. No selected-sector suppression is inferred
from the value of the complete unselected prefix near its negative-height
critical image.
