# The unselected interior integral for a mixed tangle chain

Research deduction, 7 November 2026. For any fixed word in powers
three and four, the complete finite factors determine a nonzero
asymptotic expansion on the unselected interior part of the incoming
contour. The estimate includes the entire conditional sum at each
vertex. It does not include the other Fourier choices or the rest of
the incoming period.

The result supplies a common interior calculation for arbitrary word
length. In particular the interior of the next (343) and (344)
attachments does not require a new critical-point calculation. The
remaining problem is to bound the complement in the original finite
contraction.

## 1. The exact finite functions and the part being integrated

Fix \(m\ge2\), flags \(\epsilon_j\in\{0,1\}\), and the word

\[
 (3+\epsilon_1,\ldots,3+\epsilon_m),\qquad
 k=\sum_{j=1}^m\epsilon_j.
 \tag{1}
\]

At integer level \(N\ge2\), put

\[
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j.
 \tag{2}
\]

The complete first cap and conditional polynomials are

\[
 \begin{split}
 U_{\epsilon,N}(w,X)
   &=\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(X)/P_j^{1+\epsilon},\\
 C_{\epsilon,N}(X,Y)
   &=\sum_{j=0}^{N-1}X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon}.
 \end{split}
 \tag{3}
\]

Here \(H_N\) is the original ordinary-boundary polynomial. Let \(d_N\)
be the polynomial of degree less than \(N\) satisfying

\[
                       d_N(r^a)=1/P_a\quad(0\le a<N).
 \tag{4}
\]

The exact conditional message of the word is

\[
 \begin{split}
 F_{\boldsymbol\epsilon,N}(w,X_m)
  =N^{m-1}\operatorname{CT}_{X_1,\ldots,X_{m-1}}
  \left[
   U_{\epsilon_1,N}(w,X_1)
   \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
   \prod_{j<m}\{d_N(X_j)(1+X_j^{-N})\}^{\epsilon_j}
  \right].
 \end{split}
 \tag{5}
\]

This is the repeated exact transfer in
[the conditional/Fourier identity](research_mixed_conditional_fourier_message_bridge.md).
No final Gram factor or ordinary terminal observation is included.
The term *unselected* means that one takes the factor (1), rather
than \(X_j^{-N}\), at every internal position with \(\epsilon_j=1\).
It does not delete any row from either polynomial in (3).

Use the original half-chain critical point from
[the general pre-Gram curve](research_mixed_arbitrary_prefix_pregram_curve.md),
with following external coordinate \(c\in K\), where \(K\) is any of
the four compact domains \(A_3,O_3,A_4,O_4\). Write its coordinates as

\[
 (u_*,s_{1,*},t_{1,*},s_{2,*},t_{2,*},\ldots,s_{m,*},t_{m,*}).
 \tag{6}
\]

The last vertex is an ordinary block with an external Gram incidence
to \(c\); it is not a right endpoint cap. Put \(z_*=t_{m,*}\),

\[
 P=[11/50,9/20],\qquad h_j=\Im t_{j,*},\qquad
 a_j=\Re t_{j,*}\quad(j<m).
 \tag{7}
\]

For this fixed base point define

\[
 \begin{split}
 I^{c}_{\boldsymbol\epsilon,N}(w,z)
   =N^{m-1}\int_{P^{m-1}}
    U_{\epsilon_1,N}(w,X_1)
    \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
    \prod_{j<m}d_N(X_j)^{\epsilon_j}\,dx_1\cdots dx_{m-1},\\
 X_j=e^{-2\pi i(x_j+ih_j)}\ (j<m),\qquad
 X_m=e^{-2\pi iz}.
 \end{split}
 \tag{8}
\]

All heights and endpoints in (8) stay fixed as \(w,z\) vary. This is
an exact holomorphic integral of finite polynomials. It is one part
of (5), not a replacement for that complete constant term.

## 2. The source domains and the halfweights

Every ordinary block \(j\ge2\) has external inputs

\[
 (t_{j-1,*},s_{j+1,*})\quad(j<m),\qquad
 (t_{m-1,*},c)\quad(j=m).
 \tag{9}
\]

The first left input is attached; subsequent ones are ordinary. All
right inputs lie in the corresponding \(O_3,O_4\), except for the
specified last input \(c\in K\). Thus each pair belongs to a product
covered by [the complete ordinary source theorem](research_mixed_three_row_source_assembly.md),
Section 1. This theorem was proved on the sufficient typed products,
so it also applies to the present half-chain, including \(m=2\).
No private endpoint coordinate is substituted for an ordinary input.

The first-cap input is \(s_{2,*}\). When its type is three it lies
in the permitted full type-three disk. When its type is four it lies
in the permitted reduced disk and has negative height. There is one
additional restriction if both the first and second types are four.
The ordinary block at vertex two gives

\[
 \Re s_{2,*}>259/1000,
 \qquad t_{2,*}\in P_4,
 \qquad
 c_2=\begin{cases}s_{3,*},&m>2,\\c,&m=2\end{cases}
          \in P_3\cup P_4.
 \tag{10}
\]

The first inequality is the oriented image bound for the output
adjacent to the attached type-four leg. The other two coordinates
satisfy the original inverse relations of
[the coupled first-cap domain](research_mixed_first_cap_coupled_plateau_certificate.md),
equations (1)--(2). Consequently this reference is in its
inverse-feasible set, even for the present two-vertex half-chain.
It need not satisfy the different symmetry relation of an ordinary
two-endpoint word. This verifies the extra restriction used in
[the complete cap supporting-plane theorem](research_mixed_first_cap_plateau_completion.md).

Let \(\mathcal T_{\epsilon_1}(t_1,w)\) be the calibrated cap action.
For \(j\ge2\), define the conditional action locally by

\[
 \begin{split}
 Q_{\epsilon_j}(s;t_{j-1},t_j)
  &=g(s+t_{j-1})+g(s+t_j)-(2+\epsilon_j)g(s)\\
  &\quad-g(t_{j-1})-g(t_j)+2\pi i t_{j-1}s,\\
 \psi_j(t_{j-1},t_j)&=\operatorname{stat}_s Q_{\epsilon_j}(s;t_{j-1},t_j).
 \end{split}
 \tag{11}
\]

Its critical coordinate is \(s_{j,*}\) at the base. The allocated
actions in the supporting-plane estimates are

\[
 L_1=\mathcal T_{\epsilon_1}-\frac{\epsilon_1}{2}g(t_1),\qquad
 \phi_j=\psi_j-\frac{\epsilon_{j-1}}2g(t_{j-1})
                    -\frac{\epsilon_j}2g(t_j).
 \tag{12}
\]

The cap carries the first outgoing halfweight. Each conditional
factor carries the incoming and outgoing halfweights of its two
arguments. Multiplying these estimates gives exactly one full

\[
                    |d_N(X_j)|^{\epsilon_j}
 \tag{13}
\]

at each internal argument, and the single extra factor

\[
                    |d_N(e^{-2\pi iz_*})|^{\epsilon_m/2}
 \tag{14}
\]

at the fixed last argument. When \(\epsilon_m=1\), that last
argument lies in the regular lower-half domain \(O_4\).
[Fourier weight continuation](research_mixed_fourier_weight_continuation.md)
therefore proves its nonvanishing and its uniform expansion

\[
 d_N(e^{-2\pi iz})
   =N^{-1/2}\mathcal D(z)e^{-Ng(z)}(1+O_{\rm hol}(N^{-1})),
 \qquad
 \mathcal D(z)=\frac{e^{i\pi z/2}}{\sqrt{2\sin\pi z}}\ne0.
 \tag{15}
\]

One may remove (14) using this proved lower bound. No internal
Fourier polynomial, cap, or conditional sum is divided out.

## 3. Concentration on the full independent interior box

The primitives used here are

\[
 \begin{split}
 J'(v)&=\operatorname{Log}(2\sin\pi v),\quad J(0)=0,\qquad
 g(v)=J(v)+\tfrac{i\pi}{2}(v-v^2),\\
 E(s,u)&=-2J(1/2-u)-3J(u)-J(s-u)
                +i\pi su-\tfrac{i\pi}{2}(s-s^2),\\
 V_\epsilon(s,t)&=g(s+t)-\epsilon\{g(s)+g(t)\},\\
 G(t,c)&=g(t+c)-2g(t)-2g(c)+2\pi itc.
 \end{split}
 \tag{15a}
\]

The logarithm is the continuation from the positive real sine in
the original regular strip. In (17) below,

\[
 H_{\boldsymbol\epsilon}(c)
   =\operatorname{stat}_{u,s_1,t_1,\ldots,s_m,t_m}
       \left[E(s_1,u)+\sum_{j=1}^m V_{\epsilon_j}(s_j,t_j)
              +\sum_{j<m}G(t_j,s_{j+1})+G(t_m,c)\right],
 \qquad q_{\boldsymbol\epsilon}(c)=t_{m,*}.
 \tag{15b}
\]

Here and below, \(\operatorname{stat}\) means the value at the
specified original critical point, not a maximum over other branches.

With \(t_m=z\) fixed, set

\[
 \Phi(w,t_1,\ldots,t_{m-1};z)
  =\mathcal T_{\epsilon_1}(t_1,w)
       +\sum_{j=2}^m\psi_j(t_{j-1},t_j)
       -\sum_{j<m}\epsilon_jg(t_j).
 \tag{16}
\]

Let \(\mathcal P_{\boldsymbol\epsilon}(w,z)\) be its critical
value on the original branch. At complete color, it has the exact
absolute normalization

\[
 \mathcal P_{\boldsymbol\epsilon}(-2,q_{\boldsymbol\epsilon}(c))
   =H_{\boldsymbol\epsilon}(c)
      -G(q_{\boldsymbol\epsilon}(c),c)
      -(1-\epsilon_m)g(q_{\boldsymbol\epsilon}(c)).
 \tag{17}
\]

To verify the constant and the last term, the first-cap action is
the stationary value of

\[
 E(s_1,u)+V_{\epsilon_1}(s_1,t_1)
                       -(1-\epsilon_1)g(t_1).
 \tag{18}
\]

For each subsequent block the identity of primitives is

\[
 G(t_{j-1},s_j)+V_{\epsilon_j}(s_j,t_j)
  =Q_{\epsilon_j}(s_j;t_{j-1},t_j)-g(t_{j-1})
                                      +(1-\epsilon_j)g(t_j).
 \tag{19}
\]

Substitution into (16) cancels the intermediate \(g\) terms and
gives (17). All primitives and logarithmic lifts are those of the
original action. In particular the conditional action equals the
pre-Gram row action only when the last type is four.

Write \(\mathcal F_N(w,x,z)\) for the product in the integrand
of (8), without its factor \(N^{m-1}\). The cap plane and each
ordinary plane have curvature constant

\[
                             \kappa=1/2500000.
 \tag{20}
\]

Each internal coordinate belongs to two of these planes. Their
linear terms cancel by the original stationary equations for
(16). Their constants, after removal of (14), sum to (17).
It follows that for every \(\tau>0\), at \(w=-2,z=z_*\),

\[
 |\mathcal F_N(-2,x,z_*)|
 \le C_\tau N^{B_\tau}
 \exp N\left\{\Re\mathcal P_{\boldsymbol\epsilon}(-2,z_*)
                    -2\kappa\sum_{j<m}(x_j-a_j)^2+\tau\right\}.
 \tag{21}
\]

The targets \(x_j\in P\) vary independently. Only their heights
are fixed at the base. All finite conditional rows, including
ones revived away from the physical grid, are already included
in their supporting-plane estimates.

For a fixed \(\rho>0\) whose coordinate box about \(a\) lies inside
\(P^{m-1}\), choose \(\tau<\kappa\rho^2\). Equation (21) then
gives a uniform exponential gap on

\[
              \{x\in P^{m-1}:\max_{j<m}|x_j-a_j|\ge\rho\}.
 \tag{22}
\]

The strict gap persists on a sufficiently small fixed neighborhood
of \((-2,z_*)\). For the weighted factors one first uses their
integer-weight holomorphic squares, as in the ordinary source
theorem, and then removes only the known last factor (14).
The resulting bound applies to the actual holomorphic integrand
before taking derivatives or integrating.

## 4. The nonzero asymptotic expansion and its power of the level

**Theorem.** For each fixed word (1) and each of the four compact
following families, the exact integral (8) has, on fixed sufficiently
small neighborhoods of \((-2,z_*)\),

\[
 I^{c}_{\boldsymbol\epsilon,N}(w,z)
  =N^{-1-k+\epsilon_m/2}
    \mathcal A_{\boldsymbol\epsilon}(w,z)
    e^{N\mathcal P_{\boldsymbol\epsilon}(w,z)}
       (1+O_{\rm hol}(N^{-1})),
 \qquad \mathcal A_{\boldsymbol\epsilon}\ne0.
 \tag{23}
\]

Both parities are included. The constants and local neighborhood
radii can be chosen uniformly over each compact following family
for the fixed word. Every fixed derivative of the relative error
is \(O(N^{-1})\) on smaller neighborhoods.

*Proof.* The complete cap has local power
\(N^{-1-\epsilon_1/2}\). Each complete conditional polynomial has
local power \(N^{-(1+\epsilon_j)/2}\), by
[the reduced-disk conditional theorem](research_mixed_reduced_disk_conditional_packets.md).
Every internal factor \(d_N\) of type four has (15), since its
reference is either an attached or an ordinary type-four leg.
These expansions hold on ambient neighborhoods of their actual
arguments, with nonzero holomorphic symbols. They concern the
whole finite polynomials in (3).

The negative Hessian of (16), in its \(m-1\) internal variables,
is the Schur complement obtained by eliminating the auxiliary,
private, and conditional-index variables from the original
half-chain Hessian, with the last leg fixed. The final Gram term
and the last \(g\) correction are constant in these variables.
The original negative Hessian is strictly accretive; its principal
block and this Schur complement are therefore invertible and
strictly accretive as well. For example, test the original Hermitian
form on a vector whose eliminated entries solve their linear
equations. Its value is the retained Schur form, and its real part
is positive. Thus the original real-oriented Gaussian has a
nonzero determinant and a consistently chosen holomorphic branch.

Equation (22) removes the rest of the interior box. On a small
box about the stationary point, multiply the complete local
expansions and translate the integration cycle to the nearby
stationary point when \(w,z\) vary. The additional boundary pieces
have a strict phase gap at the base and retain it by continuity.
The multidimensional Gaussian expansion now applies to this exact
finite integral.

For clarity, the level power is

\[
 \begin{split}
 &N^{-1-\epsilon_1/2}
  \prod_{j=2}^m N^{-(1+\epsilon_j)/2}
  N^{-(k-\epsilon_m)/2}
  N^{m-1}N^{-(m-1)/2}\\
 &\hspace{35mm}=N^{-1-k+\epsilon_m/2}.
 \end{split}
 \tag{24}
\]

The factors on the first line are respectively the cap, the
conditional polynomials, the internal Fourier weights, the exact
incoming density, and the final Gaussian integration. Omitting an
internal weight would change the answer.

If \(\mathcal B_{\epsilon_1}\) and \(\mathcal B_j^C\) denote
the complete cap and conditional symbols, then at the stationary
coordinates the coefficient is

\[
 \mathcal A_{\boldsymbol\epsilon}
 =\frac{(2\pi)^{(m-1)/2}
       \mathcal B_{\epsilon_1}
       \prod_{j=2}^m\mathcal B_j^C
       \prod_{j<m}\mathcal D(t_j)^{\epsilon_j}}
      {\sqrt{\det(-\Phi_{tt})}}.
 \tag{25}
\]

All its factors are nonzero and have their original branches.
The absolute action and the coefficient agree on overlapping
parameter neighborhoods by uniqueness of the original critical
coordinates. Compactness gives the stated uniformity. Cauchy's
formula for the normalized holomorphic error gives all fixed
derivatives. This proves (23). \(\square\)

For (34), (24) is \(N^{-3/2}\); for (343) and (344) it is
\(N^{-2}\) and \(N^{-5/2}\), respectively. These are powers of
the conditional normalization (5), not new normalizations of the
knot invariant.

## 5. A uniform lower bound for the conditional action

The same normalization gives an action estimate independent of word
length. At the matched coordinates of one full half-chain, let
\(\mathcal P_j\) denote the conditional action of its first \(j\)
vertices, evaluated at \(t_{j,*}\). For \(j=1\), this means
\(\mathcal P_1=\mathcal T_{\epsilon_1}(t_{1,*},-2)\).
Each cut has its actual next external leg held fixed; the different
cuts are not assigned a common external parameter.

**Proposition.** At complete color, every ordinary attachment obeys

\[
               \Re(\mathcal P_j-\mathcal P_{j-1})>1/6
                       \qquad(2\le j\le m).
 \tag{26}
\]

In particular,

\[
        \Re\mathcal P_{\boldsymbol\epsilon}(-2,z_*)
                                      >1+(m-1)/6 .
 \tag{27}
\]

This concerns the conditional action (17). The pre-Gram row action
has the additional term \((1-\epsilon_m)g(z_*)\), so (27) is not
transferred to that normalization by omission of this term.

*Proof.* Put

\[
 W(v,w)=J(v+w)-J(v)-J(w)+i\pi vw
        =g(v+w)-g(v)-g(w)+2\pi ivw .
 \tag{28}
\]

The real-height estimate and joint vertical convexity in
[terminal transform tails, Lemma 1](research_mixed_terminal_transform_tails.md),
equations (8)--(10), give

\[
 \Re W(v,w)>
    \frac15-\pi(\Re v\,\Im w+\Re w\,\Im v),
 \qquad v,w\in Q=[.23,.45]+i[-.12,.12].
 \tag{29}
\]

This is the first inequality of that proof, before its more
special endpoint-height substitution. It is valid for independent
points of \(Q\).

Also \(\Re g(x+ih)<0\) for \(0<x<1/2\) and every real \(h\).
For \(h\le0\), the disk formula

\[
 \Re g(x+ih)
     =\frac{\Im\operatorname{Li}_2(e^{2\pi h-2\pi ix})}{2\pi}
 \tag{30}
\]

is negative: its radial derivative is
\(-\arg(1-Re^{-2\pi ix})/R<0\), and its value at radius zero
is zero. At \(h=0\), continuity or the original sine integral
gives the same strict sign. For \(h>0\), Schwarz reflection of
\(J\) gives

\[
 \Re g(x+ih)=\Re g(x-ih)-\pi(1-2x)h<0 .
 \tag{31}
\]

At the \(j\)-th attachment set

\[
 y=t_{j-1,*},\qquad s=s_{j,*},\qquad z=t_{j,*},\qquad
 \alpha=\epsilon_{j-1},\quad\beta=\epsilon_j .
\]

The exact gauge in (16), or (18)--(19), gives

\[
 \mathcal P_j-\mathcal P_{j-1}
   =-\alpha g(y)+Q_\beta(s;y,z)
   =W(y,s)+W(s,z)-\alpha g(y)-\beta g(s)-2\pi isz .
 \tag{32}
\]

Consequently, writing \(x_v=\Re v\) and \(h_v=\Im v\),

\[
 \Re(\mathcal P_j-\mathcal P_{j-1})
   >\frac25+\pi\{h_s(x_z-x_y)+x_s(h_z-h_y)\}.
 \tag{33}
\]

The incoming leg \(y\) is attached at the first interface and
ordinary afterwards. Its sufficient bounds, including both roles,
are

\[
 \begin{array}{c|cc}
 \text{type of }y& x_y& h_y\text{ upper bound}\\ \hline
 3 &[.267,.433]& .068\\
 4 &[.24,.36]& -.001 .
 \end{array}
 \tag{34}
\]

The two new legs are ordinary, so they have the sharper bounds

\[
 \begin{array}{c|cc}
 \text{type of }s,z&x_s,x_z&h_s,h_z\\ \hline
 3 &[.267,.433]&[-.065,.068]\\
 4 &[.24,.36]&[-.102,-.001].
 \end{array}
 \tag{35}
\]

These are precisely the reduced disks and height cuts used above.
The lower bound for \(h_y\) is unnecessary here. The following table
bounds the negative of the braces in (33); every decimal in it is
an exact rational number.

| Incoming type | New type | An upper bound for the possible loss |
|---|---|---|
| 3 | 3 | \(.068\cdot.166+.433\cdot.133=68877/10^6\) |
| 4 | 3 | \(.065\cdot.193+.433\cdot.064=40257/10^6\) |
| 3 | 4 | \(.102\cdot.093+.36\cdot.170=70686/10^6\) |
| 4 | 4 | \(.102\cdot.120+.36\cdot.101=48600/10^6\) |

For example, in the second row \(x_z-x_y\in[-.093,.193]\).
Its worst product with \(h_s\in[-.065,.068]\) is
\(-.065\cdot.193\), since
\(.068\cdot.093<.065\cdot.193\). In the third and fourth rows
\(h_s\) is negative, so only a positive \(x_z-x_y\) can lower
the expression. The second product in each row uses the upper
bound on \(h_y\) and the lower bound on \(h_z\).

All four losses are less than \(9/125\). Hence

\[
 \Re(\mathcal P_j-\mathcal P_{j-1})
   >\frac25-\frac{9\pi}{125}
   >\frac{152}{875}>\frac16 ,
 \tag{36}
\]

where \(\pi<22/7\) was used. The complete cap theorem gives
\(\Re\mathcal P_1>1\) on the required attached images.
Summing (26) on the matched chain proves (27).
\(\square\)

## 6. What has and has not been bounded

The theorem controls all conditional indices, all private cap
indices, and the full independent incoming box in (8). In
particular it bounds the portion of that box outside any fixed
neighborhood of the geometric point. It is stronger than a local
formal saddle calculation.

There are still two omitted parts of the exact identity (5): the
incoming contour outside this box, and every nonempty choice of
the factors \(X_j^{-N}\). The theorem makes no estimate for either.
They cannot be removed merely because (23) has a nonzero leading
coefficient. For (34), the separate complete following-family
theorem supplies those additional contour bounds; for a new word
they remain to be proved. An ordinary terminal observation is a
further operation and is not included in (23).
