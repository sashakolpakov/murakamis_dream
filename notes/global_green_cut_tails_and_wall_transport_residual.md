# The global Green cut tails and the exact wall-transport residual

Research proof and independent source audit, 27 October 2026.
Integer-flow conservation excludes a direct bare wall at the final
cut before summing the two framing variables. It does not discard
internal returning wall excursions or the boundary tails produced
by Green shifts. This note records those tails, the exact residual
after the new memory contraction, and the source factor a common
wall comparison would have to produce.

These are actual source/current tests, not a geometric-period
identification or a use of scalarity of the closed knot operator.

## 1. Primitive flow elimination preserves the unsummed cut grading

Each original positive crossing sends (a,b) to (b+k,a-k), and
each negative crossing sends it to (b-k,a+k). Thus every literal
crossing term preserves the integer sum of positions, for each
transfer separately. All original diagonal pivots, Cartan phases,
zero-framing scalars and scalar moment insertions have degree zero.

Close every strand except the marked cut. Equality of input and
output positions on the closed strands forces equality at the cut
by the same integer sum. This is TERMWISE: it uses neither an
internal state sum nor a Schur argument. For a knot, primitive
flow elimination uses the unit permutation cofactor already proved
in [the actual geometric coefficient model](actual_geometric_normal_period.md).
Keep a=cut position and b=one other framing flow unsummed, and
denote all remaining free flows by t. The actual kernel therefore
has the literal form
\[
                     I(a,b,t)E_{aa}.                 \tag{1}
\]
Scalar Green moments preserve this diagonal matrix index. The
external meridian Ore shifts also preserve it. Hence the direct
final-cut image under degree elevation is diagonal and has zero
coefficient of the EXTRA root wall E_(N,0). The same statement
holds after the full Clebsch word, with all caps and lower
excursions retained: its upper final cut is E_N of this original
diagonal matrix. It is not a claim about an upper-only word.

The proof survives exact transverse SUMMATION while a,b remain
unsummed. A formal Gaussian comparison must still preserve its
external shifts, support boundaries and relative source; a bare
interior Gaussian sector does not include those boundaries.

There is a useful stronger actual charge rule. Set deg F=+1,
deg E=-1 and deg K=0. The coproduct is homogeneous in total
degree and the antipode preserves degree. Thus the TRUE Hopf
adjoint of a homogeneous h of degree d, applied to a degree-zero
word or scalar Green kernel, has degree d. Diagonal pivotal
partial trace preserves the remaining cut degree, coefficientwise
in EVERY actual q-normal order. This applies to divided powers
and their mixed coproduct terms as well.

On the actual high color r=N the fixed-head Fr wall E_(N,0)
changes the physical cut position J=NR+S by N^2. Therefore its
selected head-00 coefficient is absent for |d|<N^2. In particular
a SINGLE divided E^(N) or F^(N) current cannot create that direct
cut coefficient. The full wall head block has charges
N^2+(S_out-S_in), so is absent whenever |d|<N^2-N+1.
Dense source coupons inserted INSIDE a word change this charge
budget; an external linear co-source does not. Under a whole
source gauge the grading and every endpoint must be conjugated
together rather than freezing the old grading on new matrices.

## 2. The literal cut-window map has two missing boundary rows

Green currents are zero-extended arrays on ALL integer free flows.
A cut-index shift can therefore create tails outside 0,...,N-1.
For any such finite array retain the matrix and two exterior tails
\[
 C_Nf(b,t)=\sum_{a=0}^{N-1}f(a,b,t)E_{aa},\quad
 f_{<0},\quad f_{\ge N}.                            \tag{2}
\]
Put U=sum_(a=0)^(N-2)E_(a+1,a), and use S_+f(a)=f(a+1),
S_-f(a)=f(a-1). Exactly, with b,t still UNSUMMED,
\[
 \begin{aligned}
 C_N(S_+f)&=U^*C_N(f)U+f(N,b,t)E_{N-1,N-1},\\
 C_N(S_-f)&=UC_N(f)U^*+f(-1,b,t)E_{00}.             \tag{3}
 \end{aligned}
\]
Here star denotes the transpose partial shift in this basis,
not an additional analytic Hermitian choice. General powers have
the corresponding finite sums of r endpoint values. In particular
\[
 \frac1N\operatorname{Tr}C_N((S_+-1)f)
                         =\frac{f(N)-f(0)}N.        \tag{4}
\]
Thus compression to the finite head is NOT a translation chain
map unless its endpoint rows are included.

The correct original relative cut source is
\[
 \Phi_N^{\mathrm{rel}}(f)=\frac1N\left[
       \operatorname{Tr}C_Nf+\sum_{a<0}f(a)+\sum_{a\ge N}f(a)\right]
                       =\frac1N\sum_{a\in\mathbb Z}f(a).          \tag{5}
\]
It annihilates the complete finite difference exactly, with b,t
still unsummed. On the original kernel, whose support is in the
head window, it is the original normalized-average cut. For a
Green current the two tail sums are part of the source. Replacing
this by another high-color co-source because closed scalar periods
agree would not establish equality of these inserted rows.

Equations (2)--(5) are the explicit cut part of the source for the
[full finite Green certificate](full_certificate_framing_boundary.md).
They explain how a relative wall can arise even though (1) has
no bare off-diagonal final-cut wall coefficient. The two statements
are compatible; the wall would have to be a TRANSGRESSION of
these boundary rows, not an unproved final-matrix projection.

## 3. Bare wall trace zero does not remove returning wall excursions

The original root pivotal operator is diagonal in the head and
identity on the Fr block. Its trace on w=E_(N,0) is zero. But
the original divided Fr matrices satisfy
\[
       e^N w=N!E_{00},\qquad w e^N=N!E_{NN},
       \quad\operatorname{Tr}_{\mathrm{Fr}}(e^Nw)=N!.     \tag{6}
\]
With a literal head insertion H and pivot g_head the corresponding
closed value is N! Tr(g_head H). A paired wall can therefore
return to the degree-zero channel and survive closure. Termwise
charge conservation does not set every internal wall excursion
to zero. The strict Clebsch construction supplies actual inverse-
crossing examples of exactly such retained excursions.

For true pivotal/Hopf closure one must use the actual ordinary
generic pivot and its mixed divided coproduct. The current-level
partial-trace theorem and the frozen-pivot correction are retained
in the corresponding closure construction. No replacement of
that pivotal trace by an unweighted Fr trace is made here.

## 4. Exact residual after the new cochain contraction

Let (C,d) be the specified memory current complex, with the
actual contraction (p,i,h) onto the degree-elevation image plus
its retained wall complex:
\[
          I-ip=dh+hd,\quad pd=d_{\mathrm{red}}p,
                                      di=id_{\mathrm{red}}.           \tag{7}
\]
The explicit wall part is the already audited
[Bockstein contraction](degree_elevation_complement_bockstein_wall.md).
Let O_1,O_2 be consecutive original transported maps (crossings,
caps, projectors or source maps), and retain their actual current
defects
\[
                         \Delta_j=dO_j-O_jd.        \tag{8}
\]
For maps between different coefficient complexes the adjacent
differentials and contractions are used; external base shifts
also act on their coefficients. Nothing requires a frozen
same-base convention.

There is the exact operator identity
\[
 \begin{aligned}
 pO_2O_1i-(pO_2i)(pO_1i)
   &=d_{\mathrm{red}}H+Hd_{\mathrm{red}}
       -p\Delta_2hO_1i+pO_2h\Delta_1i,\\
 H&=pO_2hO_1i .                                    \tag{9}
 \end{aligned}
\]
Proof: insert (7) between O_2 and O_1, move d past each O_j
using (8), and use the two chain identities in (7). This proves
(9) before any summation, Gaussian expansion or scalar source.
Iterating gives a finite ordered excursion/current formula for
the entire weighted word.

For the ACTUAL relative source/ket Lambda,Psi, its scalar residual
is correspondingly
\[
 \begin{aligned}
 &(\Lambda d_{\mathrm{red}})H\Psi+\Lambda H(d_{\mathrm{red}}\Psi)\\
 &\quad-\Lambda p\Delta_2hO_1i\Psi
                         +\Lambda pO_2h\Delta_1i\Psi .           \tag{10}
 \end{aligned}
\]
The first two terms are the specified endpoint/carry co-sources,
not automatically zero. The other two are the inserted actual
intertwining currents. True pivotal naturality can remove them
for the TRUE Hopf complex with its caps; it does not identify
that complex with the MEMORY Cartan/F complex without the mixed
head and source comparison. The known Jackson off-diagonal
remainder is one explicit such inserted current.

Consequently local contraction to one wall line does not imply
that full words factor through that line. Equation (9), with
all original operators, is the finite calculation that decides it.
It is also more specific than an unspecified appeal to a regular
sequence at an isolated gluing point.

## 5. The exact co-source normalization required of a tail-to-wall map

Take the orientation of the positive boundary (4) and the normalized
selected coupled wall w tensor E_00. Its ACTUAL source value is
\[
                 \Phi_{e_D}(w\otimes E_{00})=2^{-N}.
\]
If a proposed relative comparison maps the scalar tail
t=f(N)-f(0) to c_N(t)(w tensor E_00), preservation of the original
co-source therefore FORCES
\[
                           c_N(t)=\frac{2^N}{N}t.   \tag{11}
\]
In the divided generator f^N coordinate it forces instead
2^N t/(N N!). The uniform Fr interval would require
(N+1)t/N in the w coordinate. Their ratio is exactly the already
measured 2^N/(N+1). This is a necessary coefficient equation,
not permission to choose a new normalization of the invariant.
A genuine map must derive (11) from its retained source character,
or prove that the WHOLE relevant tail class cancels. A bare
fixed algebraic unit at the Rivin point cannot account for the
exponential factor; the actual weight-N source line is essential.

The marked moment data are essential too. A coupling w^a changes
the norm of an ACTUAL translation operator T to w^N T^N. Its
finite moment derivatives retain P(a+N)-P(a), the chirp phase,
and every memory carry. This does NOT automatically replace the
Fr adjoint wall character Q^-N-1 by Q^-N w^N-1: one-sided
clock multiplication simply scales the endpoint matrix, leaving
its Ad K eigencharacter unchanged. Identifying those translation
and memory clutches is another part of the required current map,
with its Fourier/relative adapter. It must be checked, not inferred
from their equal root numerical values.

The current next test is therefore explicit: transport the two
unsummed actual Green currents through (2)--(10), including their
true pivotal caps, and evaluate their relative wall/tail pairing
at the marked Rivin branch. Its regular sequence and algebraicity
can control that evaluation once the map is supplied. They do not
determine the inserted Delta_j terms, identify the two clutches,
or supply the source factor (11). No common selected global period
line follows from the Bockstein character alone.

## 6. Independent audit: the actual divided Cartan supplies a whole wall row

The subsequent
[actual divided Ward/cap construction](actual_divided_ward_closure_and_green_caps.md)
provides a positive addition to this residual test. It passes the
following independent audit with all sources retained.

In the fixed actual beta basis the original matrices E^(N),F^(N)
preserve the residue S and move the Fr index by one. Consequently
\[
                    H(q)=\tau[E^{(N)}(q),F^{(N)}(q)]
\]
is diagonal for EVERY q, with root entries N-2R. On the extreme
Fr block its commutator is therefore entrywise multiplication by
\[
                 H_{N,s}(q)-H_{0,t}(q),             \tag{12}
\]
an original rational unit of root value -2N. Inverting these
entries gives a literal WHOLE wall extraction through the actual
Cartan commutator. It uses neither delta division nor a guessed
source comparison. The selected row remains the original one,
composed with this explicit unit inverse; its root coefficient
bound1/(2N) is not a bound replacing the wall's2^-N source.

The global current formula also checks independently. For every
actual Hopf element h,
\[
 [\rho(h),C]=\sum_{(h)}D_{h_1}(C)\rho(h_2).
\]
This follows directly from the antipode identity. Ordinary pivotal
partial trace intertwines these actual adjoints on ALL matrices.
Applying the whole weighted crossing-current identity therefore
transports (12) through an actual word, with its finite Green
difference and source row. Mixed terms of Delta H are essential;
this is not a primitive Fr or geometric-Borel assignment.

The ordinary pivot g=K and frozen pivot g_f=K^(1-N) are related
EXACTLY by P_f=chi^-1 P_o M_(Z^J). Thus the full frozen cap
defect is chi^-1 P_o[M_(Z^J),A_h]. Its first delta coefficient
is -chi_0^-1 P_(o,0)[M_J,A_(h,0)]; generator and cap derivatives
have not been omitted, since their commutators with M_0=I are
zero. The explicit E and F cap signs, the divided-adjoint q
powers and the ordered N-term telescope all check. In particular
the N small-generator rows together have order at least delta^2
before division by [N]_q!, whose zero is simple. Their individual
first normals cannot be substituted for a genuine divided cap.

Finally the construction contains a literal nonzero actual R
return, stronger than the formal trace example (6). With
m=N(N+1)-1, k=N^2 and the closed coupon E_(N,0)^Fr tensor P_head0,
only transfer k contributes to the open entry k<-0. Its first
nonzero coefficient is
\[
 [\delta^N]\,\operatorname{ptr}_K[(B\otimes I)R]_{k,0}
   =q_N^{m-2k}\,N^N N!\,
                         \eta_N^{m(m-2k)}\ne0.       \tag{13}
\]
The factorial is (-1)^k q^-k(Q;Q)_k, with root prefactor one;
its N zero factors give N! delta^N and its N nonzero blocks
give N^N. The symmetric Gaussian is a root unit1, and constant
beta phases cancel between the two legs. The frozen leading
coefficient has its additional chi_0^-1. All lower orders vanish.
The inserted coupon has physical degree N^2, so this returning
source is fully consistent with the charge restriction in Section1.

This positive whole Cartan row controls the ACTUAL finite cut
wall without changing its co-source. The remaining geometric
obligation is still to push this specified mixed Hopf/current
row and its relative Green endpoints through the partial geometric
contraction. It has not been identified with either of the two
internal geometric framing rows merely by its unit inverse.

The later
[whole Ward-grid theorem](whole_high_color_ward_grid_contraction.md)
extends this to every actual cut matrix. Its two diagonal spectra
and actual ordinary/divided F grid give a rational pole-free
contraction End to its trace center, with an explicit homotopy for
the original source. An independent proof audit checks the whole
formula, absence of off-diagonal pollution, improved comb-path
norm and two-word reduction. The root selected-source cost is
O(N^(3/2)) for r=N. Its degree-one target is the actual image of
the four rows, so no unspecified row-compatibility cokernel has
been killed. Thus the finite cut target is now completely specified;
the remaining map is the pushforward of the two internal geometric
Green/source rows into this target, with (2)--(11) retained.

[Exact cut-tail/current-contraction audit](../experiments/audit_global_green_cut_tails.py).
