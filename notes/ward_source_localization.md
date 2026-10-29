# Deleting cut roots preserves the pointed relative Ward class

Research proof, 27 October 2026. The original cut covector does not
descend after deleting the root `A=1`. A different literal finite cut
does descend, and its matrix functional is explicitly cochain
homotopic to the original on the actual Ward complex. The equivalence
extends to the relative boundary resolution and to a marked whole
normal family. It is a boundary/source comparison, not a rule for
compressing crossings or a geometric Gaussian source-survival theorem.

## 1. The localized source and its exact normalization

Fix `N>=2`, `Q` primitive of order `N`, and the original evaluation
color `V=C_N=k[A^+/-1]/(A^N-1)`. In its evaluation basis the source
is `psi=(1,...,1)^t`, the co-source is `phi=(1/N)(1,...,1)`, and
`e=psi phi`. Let `S` be any nonempty set of retained roots,
`m=|S|=N-s>0`, and let `P` be multiplication by its characteristic
idempotent. Define

    psi_S=P psi, phi_S=(N/m)phi P,
    e_S=psi_S phi_S=(N/m)P e P.                   (1)

One has `phi_S psi_S=1`, `e_S^2=e_S`, and `Tr e_S=1`. The
literal new matrix cut is

    Phi_S(C)=Tr(e_S C)=(1/m)sum_(a,b in S) C_(a,b). (2)

The factor `N/(N-s)` is retained exactly, for every `s<N`. The
original pivot and marked defect remain available via
`Phi(C)=Tr(g D C)`; equation (2) changes the boundary representative,
not the original numerical invariant on closed tangles. The entire
external full-ADO factor remains unchanged.

For deletion only of `A=1`, let `epsilon_1=(1/N)sum_(j<N)A^j` and
`P=1-epsilon_1`. The new color co-source is intrinsically

    phi_S(f)=[N phi(f)-f(1)]/(N-1).               (3)

It kills the deleted root's entire idempotent summand and factors
through `C_N[(A-1)^(-1)]=P C_N`. Thus it removes the previously
displayed localization obstruction for this new representative.

## 2. The actual Ward homotopy, on all matrices

Use the actual root matrices `K,F` and the split image Ward complex
from [the Ward contraction](actual_borel_ward_cut_contraction.md):

    W_N^0=End(V), W_N^1=im delta_N,
    delta_N(C)=([K,C],[F,C]),
    h_N delta_N=I-i_N p_N, delta_N h_N=I,
    p_N(C)=Tr(C)/N, i_N(c)=c I.

Both `Phi` and `Phi_S` take value one on `I`. Consequently

    Phi_S-Phi=(Phi_S-Phi) h_N delta_N.            (4)

This is an explicit all-matrices cochain homotopy, with the known
finite denominators in `h_N`. Every actual closed cut tangle is
Ward closed and equals `F_N(M)I`. Hence

    Phi_S(C_K)=Phi(C_K)=F_N(M).                   (5)

This holds wherever that original root-color cut operator is defined,
as a meromorphic whole germ in `M`; no scalar or peripheral factor
is replaced by its value at completeness.

The distinction between the two source complexes matters. In the
color relative complex `R(C_N)` alone, `phi_S` and `phi` are not
homotopic: its top cohomology is `C_N`, and they have different
values on `epsilon_1`. Equation (4) uses the **matrix Ward**
differential. It must not be presented as a homotopy in the old
color relative complex without that additional differential.

## 3. An explicit localized Ward complex and retraction

Order the retained labels as `a_1<...<a_m`. Put `V_S=P V` and
`K_S=K|_(V_S)`. If several interior roots were deleted, the ordinary
compression of `F` can be disconnected. Instead use the specified
skip-transport matrix

    (F_S)_(a_(j+1),a_j)=product_(r=a_j)^(a_(j+1)-1)(1-Q^(r+1)),
                           1<=j<m.             (6)

All these coefficients are units. This is the original F transport
along the unique retained linear interval between the two labels.
For deletion only of label zero it is ordinary compressed `F`.
For `m=1` it is zero, as appropriate to a one-dimensional space.

The distinct `K_S` eigenvalues and the connected nonzero path (6)
give `ker delta_S=k I_S`. The same entrywise and cumulative formulas
give its explicit split image Ward complex `W_S` and contraction
`h_S`, with normalized row `p_S=Tr/m`.

Let `L:V->V_S` be restriction and `J:V_S->V` be inclusion, so
`JL=P,LJ=I_S`. Define

    c_0(C)=L C J,
    c_1=delta_S c_0 h_N.                         (7)

Then `c_1 delta_N=delta_S c_0`: the only omitted term is
`delta_S c_0 i_N p_N=0`. Thus (7) is a genuine chain map, not an
assumed rowwise compression of Ward currents. It sends `I_N` to
`I_S` and induces the identity on scalar cohomology.

A section is equally explicit. Set

    s_0(T)=J T L+p_S(T)(I_N-P),
    s_1=delta_N s_0 h_S.                         (8)

It is a chain map, sends `I_S` to `I_N`, and `c s=I` in both
degrees. With `H=(I-s_0 c_0)h_N` in degree one, direct multiplication
gives

    H delta_N=I-s_0 c_0,
    delta_N H=I-s_1 c_1.                         (9)

Therefore deleting any `s<N` roots gives an explicit homotopy
retraction of these Ward complexes. The localized cut on `W_S`
composed with `c_0` is exactly (2).

This construction transports currents as well as the scalar class.
It does not turn `V_S` into the original quantum-group module.
The skip matrix is a Ward transport operator; no coproduct, crossing
intertwining, or Hopf-pivotal property is inferred for it.

## 4. The relative source map is strict after adjoining Ward currents

For a coefficient space `E`, the existing relative source resolution
is `R(E)=R(k) tensor E`, where

    R(E)^1=E[t],
    R(E)^2=E[t] direct_sum E direct_sum E,
    d_R h=(partial_t h,h(0),h(1)).

Its contraction is natural for every linear coefficient map.
Apply it degreewise to `W_N` and `W_S` and use the usual total
differential `d_R tensor I+(-1)^degR I tensor delta`. Equations
(7)--(9) extend to actual relative-Ward chain maps and homotopies.
The two cut rows extend to maps into `R(k)`; their homotopy is
explicitly

    r tensor x -> (-1)^deg(r) r tensor
                              [(Phi_S-Phi)h_N](x).

Thus the **combined** relative-Ward complex has the same nonzero
pointed line after deletion. This is a precise relative source
extension of (4), rather than just equality on one knot value.

## 5. The whole normal and its branch mark can be retained

Let `R=k[[U-1]]`, and retain the actual finite color normal algebra

    C_U=R[A]/(A^N-U).

Mark the unique root `alpha(U)^N=U`, `alpha(1)=1`. Its evaluation
branches are `A=alpha(U)Q^a`. The idempotent

    epsilon_0(U)=(1/N)sum_(j=0)^(N-1)(A/alpha(U))^j

is regular and projects onto the marked branch reducing to `A=1`.
Put `P(U)=1-epsilon_0(U)`. The exact whole-normal co-source is

    phi_S,U(f)=[Tr_(C_U/R)(f)-f(alpha(U))]/(N-1)
             =Tr_(P(U)C_U/R)(P(U)f)/(N-1).        (10)

It is regular, normalized on `P(U)`, and retains every normal
coefficient. Since `A-1` is a unit on the retained summands,
(10) factors through `A-1` localization. The marked deleted branch
is removed as a whole; its punctured generic remnant is not used
to divide away its normal contribution.

For a canonical representative `f_tilde=sum_(j<N)f_j A^j`, equation
(10) reads `[N f_0-f_tilde(alpha)]/(N-1)`. Multiplication still has
the exact carry

    A f_tilde-(Af)_tilde=f_(N-1)(A^N-U).

The source is linear, and this carry remains necessary. Deletion
repairs the excluded-root obstruction; it does not make a trace
functional into a ring map or erase the normal `U`.

The same marked construction works for any subset of branches.
In the split evaluation lattice one can use
`K_aa=x alpha^(-1)Q^(-a)` and the interior path entries
`F_(a+1,a)=1-alpha Q^(a+1)`. They specialize to the original
matrices. Distinct K differences and these interior path entries
are units over `R`. A separately specified cyclic wrap can also be
retained; it does not enter the interior entries used by the Ward
contraction. The retractions above therefore extend over this
whole formal boundary normal family, with their normalization
`N/(N-s)` unchanged. No Hopf or internal-network extension is
inferred from this boundary construction.

## 6. Compression has an exact composition defect

For arbitrary matrices `C,D`, one has

    c_0(CD)-c_0(C)c_0(D)=L C(I-P)D J.             (11)

The right side records an excursion through the deleted root
sector. It is generally nonzero. Thus independently compressing
each crossing, turn, or cap does not reproduce compression of
the whole actual network. Nor is `c_0` multiplicative or an
ordinary quantum-group intertwiner. The current map (7) is the
specific repair in the split Ward complex; it supplies no local
R-matrix replacement or strict tensor functor.

The old statement that the **original** co-source fails to descend
is still correct. The new result is that its pointed relative-Ward
class has a literal representative supported on the geometric open
chart, with an exact normalization and a marked whole-normal
extension. A source-compatible internal Gaussian comparison can
use this representative and its homotopy. Such a comparison must
still transport the excursion currents, carries, and the other
retained divisors. Nonzero geometric-source survival and the
volume conjecture do not follow just from deleting the root.

[Exact audit](../experiments/audit_ward_source_localization.py)
and [results](../experiments/ward_source_localization_results.json)
check the source homotopy and explicit chain retraction on matrix
units, for every nonempty retained subset at seven levels. They
also retain a nonzero compression-excursion defect and the marked
whole-normal carry.

[Independent proof audit](ward_source_localization_independent_audit.md).
