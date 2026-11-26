# Exact endpoint regrouping across a finite partition of windows

Private written proof, 17 November 2026.

The midpoint Fourier pairing of a finite union of cells has one
literal endpoint formula. Its auxiliary cubic packets cancel before
any estimate. At an internal cut, the two signed endpoint chains join
into a single chain carrying the difference of the neighboring scalar
representatives divided by the original spectral relation. Shared
physical jets make this quotient holomorphic through the overlap rows.

Passing from separate cell pairings to this union pairing changes the
exterior half-boundaries. The cross-window Fourier terms are exactly
compensated by that change; they are not omitted. The top pieces have
the original unit-charge estimate. The internal quotient chains and
the external endpoint terms remain in the original joint closing.

## 1. Partition, scalar data and the common spectator

Use the centered angular coordinate and a finite consecutive partition
\[
 X_j=(j+\tfrac12)/N,\qquad a_l=k_l/N,
 \quad k_0<k_1<\cdots<k_s,
 \quad I_l=[a_{l-1},a_l],\quad I=[a_0,a_s].             \tag{1}
\]
The number \(s\) is fixed. Cell lengths are bounded above and below
by fixed positive constants. Midpoint rounding may depend on \(N\).
Let \(J_l=\{k_{l-1},\ldots,k_l-1\}\).

For each cell let \(f_l\) be the actual normalized scalar error
representative, with exact data
\[
             d_j=f_l(X_j),\qquad e_j=f_l'(X_j)
                                  \quad(j\in J_l).    \tag{2}
\]
All cells use the same analytic phase weight \(S_N\) and the same
unchanged weighted spectator
\[
 A_N(X)=e^{NS_N(X)}\sin(2\pi X)P_N^{\rm sp}(X).        \tag{3}
\]
The spectator includes the original filling carrier, shared factors
and all remaining closing data. It is not the spectral relation.
For a product at a shared vertex, (2) means the full ordinary product
normal after subtracting \(NS_N'\) times the value. Independent
normal channels are not assumed scalar-compatible.

Set
\[
 \begin{split}
 c_l(\xi)&=\sum_{j\in J_l}
       [e_j-2\pi iN\xi d_j]e^{-2\pi iN\xi X_j},\\
 \widehat A_r(\xi)&=\int_{I_r}A_N(z)e^{2\pi iN\xi z}\,dz,\\
 P_{lr}&=\pi N\int_{-1}^1c_l(\xi)\widehat A_r(\xi)\,d\xi,\\
 P_U&=\pi N\int_{-1}^1
        \left(\sum_lc_l(\xi)\right)
        \left(\sum_r\widehat A_r(\xi)\right)d\xi
       =\sum_{l,r}P_{lr}.
 \end{split}                                           \tag{4}
\]
Thus \(P_U\) uses one common spectator transform over the union.
The separate cell pairings give only \(\sum_lP_{ll}\). The cross terms
\(P_{lr}\), \(l\ne r\), are part of the exact union pairing.

All statements can be made coefficientwise in the remaining variables
and with fixed ordinary derivatives on admitted buffers. The original
joint closing is denoted by \(\Lambda_N\).

For the ordinary positive-window source normalization below, the cells
contain one angular lift of each selected double physical node and
avoid the odd center. The Fourier and contour identities themselves
are valid for arbitrary intervals (1). A source application including
the odd center uses the full mirrored window and the half normalization
specified after (9).

## 2. The exact change of exterior half-boundaries

For \(\sigma=\pm1\), form the normalized one-sided cardinal error
\[
 H_l^\sigma(X)=\sum_{j\in J_l}
   \{d_j+(e_j-\sigma2\pi iN d_j)(X-X_j)\}
       e^{\sigma2\pi iN(X-X_j)}
                  \operatorname{sinc}^2(N(X-X_j)),     \tag{5}
\]
where \(\operatorname{sinc}v=\sin(\pi v)/(\pi v)\).
Its values and first angular derivatives are exactly \(d_j,e_j\)
at the nodes of \(J_l\), and both vanish at every other centered
grid node. This follows from the double zeros of the squared sinc.
The factor multiplying \(X-X_j\) removes the derivative of the
one-sided exponential at its own node.

Let \(\mathcal E_{lr}\) denote the exterior half-boundary term for
the pair \(e^{NS_N}H_l^\pm\) on cell \(I_r\), before the remaining
closing and with the ordinary positive-window normalization of the
pinned midpoint identity. Keep all its vertical sides. That identity
gives
\[
 Z_{lr}=\mathcal E_{lr}-\eta\pi^{-2}P_{lr},
                     \qquad\eta=(-1)^{N-1}.            \tag{6}
\]
Here \(Z_{lr}\) is the literal local angular-residue functional of
the error data of (5) on \(I_r\), with the original spectator. For
\(l\ne r\) these data vanish, so
\[
              Z_{lr}=0,\qquad
              \mathcal E_{lr}=\eta\pi^{-2}P_{lr}.      \tag{7}
\]
The same midpoint Fourier proof applies even when the nodes defining
(5) lie outside \(I_r\): the sine kernels still vanish at its midpoint
endpoints. No external node residue is enclosed.

**Proposition 1.** Let \(\mathcal E_U\) be the exterior half-boundary
term for the union representative \(\sum_lH_l^\pm\). Then exactly
\[
 \mathcal E_U=\sum_{l,r}\mathcal E_{lr},\qquad
 \mathcal E_U-\sum_l\mathcal E_{ll}
                     =\eta\pi^{-2}\sum_{l\ne r}P_{lr}, \tag{8}
\]
and hence
\[
 \sum_l Z_{ll}
       =\mathcal E_U-\eta\pi^{-2}P_U.                  \tag{9}
\]
After \(\Lambda_N\), this is the same original tensor cell error
contribution. The common baseline has not been included in \(f_l\).

**Proof.** For a fixed \(l\), subdivide each exterior half-contour
over the union into the cell half-contours. Their internal vertical
sides have opposite orientations and the same function \(H_l^\sigma\),
so they cancel exactly. Sum over \(l\) to obtain the first equality
in (8). Equation (7) gives its second equality. Finally use (4),(6)
to prove (9). Linearity permits the unchanged remaining closing.
This is a finite full-jet source argument; it asserts no useful
off-grid bound on the union cardinal representative. \(\square\)

At a mirrored angular normalization the same identities carry the
original common factor of one half. A simple odd spectral node uses
only its value; an angular derivative specified by an actual scalar
completion is auxiliary and does not impose an additional spectral
normal. The identities may also be applied on bulk windows separately
from that fold. No first-angle parity of (5) is assumed.

## 3. Removing the auxiliary cubics exactly

Use the kernels of the pinned coherent-alias theorem:
\[
 W_{\sigma,N}(y)=-\sigma
       \frac{e^{2\pi i\sigma Ny}}{(1+e^{2\pi i\sigma Ny})^2},
 \qquad
 L_N(z-y)=\int_{-1}^1 e^{2\pi iN\xi(z-y)}d\xi .       \tag{10}
\]
The entire kernel \(L_N(s)=\sin(2\pi Ns)/(\pi Ns)\) has value two
at zero. Fix \(H>0\), and suppose \(f_l\) is holomorphic on a buffered
rectangle over \(I_l\) of heights \([-H,H]\). At neighboring cells
these domains overlap in a buffered rectangle around their cut.
Define
\[
 \begin{split}
 T_{l,\sigma}&=[a_{l-1}+i\sigma H,a_l+i\sigma H],\\
 V_{c,\sigma}&=[c,c+i\sigma H],\qquad
 \mathcal C_N=-2\pi^2iN^3.
 \end{split}                                           \tag{11}
\]
There are no poles of \(W_{\sigma,N}\) on these top or midpoint
vertical segments.

**Lemma 2.** For every analytic scalar \(f_l\), without endpoint
vanishing assumptions,
\[
 c_l(\xi)=-2\pi iN^2
  \sum_{\sigma=\pm1}
   \int_{T_{l,\sigma}+V_{a_{l-1},\sigma}-V_{a_l,\sigma}}
        f_l(y)e^{-2\pi iN\xi y}W_{\sigma,N}(y)\,dy.    \tag{12}
\]

**Proof.** As meromorphic functions,
\[
 W_{-,N}=-W_{+,N},\qquad
 W_{+,N}(y)=-\frac1{4\cos^2(\pi Ny)}.                 \tag{13}
\]
The sum of the upper and lower chains in (12), with these weights,
is the negative of the positive rectangle contour weighted by
\(W_{+,N}\). At a centered physical node its principal part is
\(-1/[4\pi^2N^2(y-X_j)^2]\), with no simple term. The residue of
\(f_l(y)e^{-2\pi iN\xi y}W_{+,N}(y)\) is therefore
\[
 -\frac{[f_l'(X_j)-2\pi iN\xi f_l(X_j)]
                        e^{-2\pi iN\xi X_j}}{4\pi^2N^2}.
\]
The residue theorem with the stated negative orientation gives
(12), including its sign and factor. \(\square\)

Equivalently, subtract the actual endpoint cubic from each \(f_l\)
as in the pinned alias theorem. Apply (12) to that cubic and add
its formula to the already proved formula for the zero-endpoint
remainder. The cubic's own Fourier packet cancels its subtracted
contour terms exactly. Thus (12) is the no-cubic form of that theorem,
not an estimate discarding endpoint jets.

For oriented chains write
\[
 \mathcal J_\sigma[f;Y,Z]
   =\int_Y\int_Z f(y)A_N(z)W_{\sigma,N}(y)L_N(z-y)
                                                   \,dz\,dy.   \tag{14}
\]
All integrals below are finite and over the displayed actual chains.

## 4. The joint endpoint formula

Choose the spectator contours \(\gamma_\sigma\) as in the alias theorem,
now for the entire interval \(I\). They have bounded length, connect
\(a_0+i\sigma h_{0,\sigma}\) to
\(a_s+i\sigma h_{s,\sigma}\), and satisfy
\[
            0\le\sigma\Im z\le H,
               \qquad 0\le h_{0,\sigma},h_{s,\sigma}\le H.
                                                               \tag{15}
\]
The deformation and endpoint connectors remain in the actual
holomorphy domain of \(A_N\). Put
\[
 E_\sigma=[a_0,a_0+i\sigma h_{0,\sigma}]
                   -[a_s,a_s+i\sigma h_{s,\sigma}].    \tag{16}
\]
Thus \(I\) and \(\gamma_\sigma+E_\sigma\) have the same holomorphic
integrals. Crossed poles, if any are admitted instead, contribute
their original residues to the endpoint formula.

At each internal cut define
\[
 \delta_l=f_{l+1}-f_l,\qquad
 S_l=[a_l-iH,a_l+iH],\qquad1\le l<s.                  \tag{17}
\]

**Theorem 3.** Exactly
\[
                      P_U=B_U+O_U+\sum_{l=1}^{s-1}J_l,\tag{18}
\]
where the top term is
\[
 B_U=\mathcal C_N\sum_{l,\sigma}
                \mathcal J_\sigma[f_l;T_{l,\sigma},\gamma_\sigma],
                                                               \tag{19}
\]
the complete external packet is
\[
 \begin{split}
 O_U=\mathcal C_N\sum_{\sigma=\pm1}\{&
    \mathcal J_\sigma[f_1;V_{a_0,\sigma},I]
   -\mathcal J_\sigma[f_s;V_{a_s,\sigma},I]\\
   &+\sum_l\mathcal J_\sigma[f_l;T_{l,\sigma},E_\sigma]\},
 \end{split}                                           \tag{20}
\]
and each internal packet is the single chain
\[
 J_l=\mathcal C_N\int_{S_l}\int_I
       \delta_l(y)A_N(z)W_{+,N}(y)L_N(z-y)\,dz\,dy.    \tag{21}
\]
The representative in (21) is holomorphic at its real crossing
under the overlap hypotheses in Section 5. Without those hypotheses,
the displayed straight chain still avoids physical poles at its
midpoint real crossing, but no unrestricted deformation is asserted.

**Proof.** Substitute (12) in the union pairing (4), interchange its
finite sums and integrals, and perform the \(\xi\) integral. Its
coefficient is precisely \(\mathcal C_N\). The right vertical of
cell \(l\) and the left vertical of cell \(l+1\) combine into
\(\delta_l\) on each signed segment. By (13),
\[
 \int_{a_l}^{a_l+iH}\delta_l W_{+,N}(\cdot)\,d(\cdot)
 +\int_{a_l}^{a_l-iH}\delta_l W_{-,N}(\cdot)\,d(\cdot)
       =\int_{a_l-iH}^{a_l+iH}\delta_l W_{+,N}(\cdot)\,d(\cdot).
                                                               \tag{22}
\]
This remains true with the entire kernel and the spectator integral
included. Only the leftmost and rightmost verticals are unpaired.
For the top terms, deform the common spectator interval to
\(\gamma_\sigma+E_\sigma\). Leave the internal and outer vertical
terms paired with \(I\). This proves (18)--(21), without omitted
endpoint cross terms. \(\square\)

In particular the real point \(a_l\) is not an endpoint of the
combined internal chain. Its two endpoints are at the top and bottom.
The jumps at the cuts have not been declared zero merely because the
nearby nodal data agree.

## 5. Exact overlap division and charged top bounds

Suppose neighboring scalar representatives have the same physical
values and first angular normals at every row in their enlarged
overlap. In the actual short spectral construction this follows from
the exact two-line targets; one changes one vertex label at a time,
with all other source labels fixed. With
\[
 C(y)=2\cos(2\pi y),\qquad
 \mathcal P_N(z)=2T_N(z/2)+2,
 \quad\mathcal P_N(C(y))=4\cos^2(\pi Ny),              \tag{23}
\]
the normalized jump satisfies
\[
       \frac{\delta_l(y)}{\mathcal P_N(C(y))}
                  \quad\hbox{holomorphic on the overlap}.       \tag{24}
\]
Here the overlap is an admitted domain containing only shared
physical rows among its real grid points. The common analytic phase
is a unit, so normalizing does not alter the order of vanishing.
For spectral representatives, the odd simple node has a simple
spectral zero and hence a double angular zero; no extra normal is
needed. All required derivatives in the remaining parameters retain
this division.

Using (13),(23), (21) becomes exactly
\[
 J_l=2\pi^2iN^3\int_{S_l}
       \frac{\delta_l(y)}{\mathcal P_N(C(y))}
       \left\{\int_I A_N(z)L_N(z-y)\,dz\right\}dy.     \tag{25}
\]
The braces are entire in \(y\) for the fixed compact spectator chain.
Thus the shared-node quotient is precisely the internal endpoint
current, with a definite normalization, rather than an analogy to it.
The pinned overlap-transport theorem applies to this holomorphic
coefficient, including its remaining spectators. Contours with the
same top and bottom endpoints can be deformed within that overlap
without a physical-row residue. Moving those endpoints adds their
actual connectors. Further poles and joint boundary faces remain.
In particular a larger detour enclosing nonshared rows requires their
actual residue packet: the overlap ideal is not the full-grid ideal.

Suppose additionally, on the buffered cell rectangles,
\[
                   |f_l|\le e^{-\kappa N+o(N)},
                         \qquad\kappa>0,              \tag{26}
\]
uniformly for the fixed finite collection. The same kernel estimate
as in the coherent-alias theorem gives
\[
 |B_U|\le e^{-\kappa N+o(N)}
       \sum_{\sigma=\pm1}\int_{\gamma_\sigma}
                 |A_N(z)|e^{-2\pi N|\Im z|}|dz|.      \tag{27}
\]
Indeed on each top, \(|W_{\sigma,N}L_N(z-y)|\le
2(1-e^{-2\pi NH})^{-2}e^{-2\pi N|\Im z|}\); the finitely many
lengths and powers of \(N\) are subexponential. This uses the actual
unit-charge phase, including the original quadratic filling carrier
and the unit character in the pinned alias theorem. If that entire
spectator contour weight has a supplied parent bound \(e^{NB+o(N)}\),
then the top term has rate at most \(B-\kappa\).

Equation (27) does not estimate (20) or (25). In particular the
Fourier kernel in the braces of (25) must remain with its common
spectator. A contour connecting the two heights can pass through
small height, where a separate absolute estimate would restore the
uncontrolled real spectator rate. Holomorphic division permits
transport; it does not supply the required coupled action bound.

## 6. The unchanged joint source and its baseline

Combining (9),(18) yields, in the ordinary positive normalization,
\[
 \boxed{\quad
 Z_{U,N}=\Lambda_N\!\left[
   \mathcal E_U-\eta\pi^{-2}
        \left(B_U+O_U+\sum_{l=1}^{s-1}J_l\right)\right].
 \quad}                                                        \tag{28}
\]
Every crossing, shared-color derivative and external polynomial stays
inside this original closing. Its mirrored version has the original
half multiplicity described after (9). Formula (8) explicitly tracks
the changed exterior half-boundaries from separate cells; in
particular (28) cannot be combined with the old separate exterior
sum while dropping the cross-window pairings.

Because the \(f_l\) are errors, \(Z_{U,N}\) in (28) denotes the
covered error-data trace, not the covered baseline. Let
\(Z_{U,N}^{\rm base}\) be the original finite residue functional of
the common baseline data on the covered rows, and let \(Z_{O,N}\)
contain the unchanged unmatched rows. The actual source is
\[
 Z_N=Z_{O,N}+Z_{U,N}^{\rm base}
       +\Lambda_N\!\left[\mathcal E_U-\eta\pi^{-2}
                    \left(B_U+O_U+\sum_lJ_l\right)\right].
                                                               \tag{28a}
\]
This is an equality of full physical jets and their original closing;
it does not identify the baseline with a canonical free polynomial.
In particular, writing \(c=\eta\pi^{-2}\), the regrouping of the
outer packet is exactly
\[
 Z_{O,N}+Z_{U,N}^{\rm base}+\Lambda_N(\mathcal E_U-cO_U)
               =Z_N+c\Lambda_N\!\left(B_U+\sum_lJ_l\right).
                                                               \tag{28b}
\]
Thus the unmatched rows plus outer terms are not merely an unmatched
row source: the displayed matched top and internal contributions
remain, with the plus sign in (28b).

The exterior endpoints of the union, unmatched physical rows and
all other current faces remain outside this regrouped window. For
several variables, the finite source equalities may be applied
successively with the other variables retained; any subsequent joint
homotopy keeps its complete relative boundary. No independent closing
of the Fourier factors is used. The result proves the endpoint
regrouping and the top bound, not a global parent-action estimate or
a nonzero geometric coefficient.

## Direct sources and author audit

The complete direct texts are:

* [Midpoint Fourier/normal pairing](research_leaf_interface_midpoint_fourier_pairing.md),
  SHA256 d24bf81b7ab841022ec72fb1e6af2d76e03aea057f749c0e60d350e200784083:
  exact cell/window closing, shared products and exterior half-boundaries.
* [Coherent alias transport](research_coherent_window_fourier_alias_transport.md),
  SHA256 dd7e429f0ed6b1b7ea93b92358417fbff1d38082cc2fe287c038505efad074de:
  scalar compatibility, original charge, finite cubic/endpoint packets
  and the two-sided top-contour estimate.
* [Overlapping spectral seams](research_overlapping_spectral_window_seam_transport.md),
  SHA256 b19521e052b2e5db60abed1a284600467c7df56e319f4ebd8b29213ccfd481c7:
  actual full shared-node ideal, exact tensor source scope, removable
  quotient transport and all retained connectors and faces.

Only written mathematics and source-text/hash reads are used.
No mathematical program, numerical computation, test or compilation
is run. Adopted and public notes remain unchanged.
