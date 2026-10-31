# Independent audit of the two physical cuts, bands and selected source

27 October 2026. The two-cut route gives a genuine two-position
source/current model. It escapes the one-cut diagonal obstruction,
has a unimodular flow chart, and supplies canonical nonzero LOCAL
Gaussian blocks for bounded port offsets. The global selected-class
comparison still needs its specified endpoint/projector and sheet
data. The assertions below distinguish these operations explicitly.

## 1. Integral physical coordinates and the original source

The existence/lattice proof in
[the actual two-cut construction](actual_two_cut_framing_port_reconstruction.md)
passes independently. Edge differentials here mean logarithmic
physical-clock differentials on the classical critical scheme;
integer labels define the underlying flow lattice. If all edge
differentials lay in the span of the first cut differential, so
would all transfer differentials, contradicting the two-dimensional
critical framing tangent space. A second independent physical edge
therefore exists on an open chart.

For a connected graph G with circulation lattice L, the kernel
of evaluating a set S of edge flows is the circulation lattice
of G minus S. Incidence ranks give exactly
\[
       \operatorname{rank}\mathrm{ev}_S=|S|+1-c(G\setminus S).
\]
Rank two for the chosen pair implies that its complement is
connected. A spanning tree avoiding both edges gives an integral
fundamental-cycle basis with these two flows as literal coordinates.
Thus there is no finite lattice index, congruence loss, extra cover
or Jacobian factor. All zero-extension support conditions move
with that integer change of variables.

Opening the second identity wire means replacing it by the literal
matrix unit E_bd. Summing E_bb restores its identity. Every original
pivotal/turn/framing/peripheral tensor stays in its original place;
no second pivotal weight is added. The reconstruction T_(a,b)^(c,d)
and its double diagonal J_ab therefore have the exact source
\[
                      F_N=\frac1N\sum_{a,b}J_{ab}.   \tag{1}
\]
Use RAW coefficients for J. If the old Green array already includes
1/N, multiply its partial reshape by N before applying (1).
There is no second normalization 1/N.

J is a linear reshaping, not the two-leg operator algebra. For
example diagonal extraction of the identity on H tensor H is
the all-ones matrix, whose source value in (1) is N, while the
actual two-cut unknot is the swap tensor and gives J=I, value one.
A trace-center or multiplicative statement about J cannot silently
be imported from the original four-port operator.

## 2. The whole two-flow Green/source complex passes

The [matrix/Laurent/coherent construction](two_cut_matrix_green_and_coherent_source.md)
passes independently. The four signed shift formulas retain the
correct row/column tails, and their composition retains the common
corner. Its Laurent kernel includes ALL finite tails. Consequently
source evaluation F(1,1)/N kills full zero-extended differences,
while window restriction has precisely its displayed boundary rows.

For d_x=x^-1-1,d_y=y^-1-1 the displayed h_0,h_1 satisfy all three
contraction identities with their printed signs. The identity-matrix
anchor is correct too: Gamma=h_0(E_N-N) has differential E_N-N,
so subtracting Gamma times the original source changes the section
to E_N without changing the other identities. It does not introduce
1/N^2 or declare every physical tangle to have that anchor.

The P1 kernel uses the literal uniform source and dual, not binomial
coherent weights. Its input clock is a ONE-FORM pullback w to w/Q:
the differential factor cancels the extra Q, giving exactly Q^b.
The finite Laurent principal parts remain in their nine tensor
regions; projecting to a finite Serre quotient would discard the
tails and is not done.

The generating variables are dual weights, not physical positions:
\[
 \mathscr F(x,y)=\sum J_{ab}x^ay^b,\qquad
 Q^a\leftrightarrow[x\mapsto Qx],\quad
 S_a^+\leftrightarrow x^{-1}.                     \tag{2}
\]
Rivin's physical coordinates are A=Q^a,B=Q^b. Identifying (x,y)
with (A,B) would change the problem. Source evaluation at x=y=1
is the original zero-weight framing pairing.

## 3. Actual port currents have an exact band extension

For fixed literal port order retain
\[
 J^{p,q}_{ab}=T_{a+p,b+q;a,b},
\]
with zero values outside all four physical ranges. If
E e_j=e_j^{E}e_(j-1) and F e_j=f_j e_(j+1), direct matrix
multiplication gives the first-port commutator identities
\[
 \begin{split}
 [E_1,T]^{p,q}_{ab}
  &=e^E_{a+p+1}J^{p+1,q}_{ab}
                         -e^E_aJ^{p+1,q}_{a-1,b},\\
 [F_1,T]^{p,q}_{ab}
  &=f_{a+p-1}J^{p-1,q}_{ab}
                         -f_aJ^{p-1,q}_{a+1,b}.    \tag{3}
 \end{split}
\]
The second-port formulas interchange (a,p) and (b,q). Arbitrary
port matrices have the stated sums of such shifted bands. This is
a lossless finite current map, including the genuine endpoint
coefficients and all original phase marks.

For every current tensor the original source is
\[
 \Phi^{(2)}(T)=\sum_{p,a,b}(e_0)_{a,a+p}J^{p,0}_{ab}.
                                                               \tag{4}
\]
In the balanced frame (e_0)_ij=1/N. A homogeneous cut degree d
selects p=d; only a conserving scalar kernel selects p=q=0.
Thus (1) may not be used as the source of every off-diagonal
Hopf current. The actual two-cut unknot already proves that a
single-port E action does not descend to ordinary left EJ:
its diagonal extraction is zero, whereas EJ=E is nonzero.

The actual insertion identity (3.1) in the main construction
passes: A and B intertwine their ACTUAL intermediate coproducts,
so the true adjoint of A X B is A(ad X)B, and the genuine pivotal
cap is natural. Its E prefix terms and F cancellations have the
correct order and weight k_X. For weighted words retain their
extra crossing currents; for the frozen cap retain its exact
moment-clock defect. A naive Delta on the reshaped J is not used.

In a specified parallel two-leg Delta convention, the source of
an ordinary E row needs only J^(0,0) and J^(-1,+1); F needs
J^(0,0) and J^(+1,-1). This follows by (3) applied to the actual
coproduct. A word of r ordinary E/F generators accesses exchange
bands |p|<=r. For arbitrary boundary ordering this statement must
first be transported by its actual opposite/dual/braided port
dictionary. The literal cut tensor is NOT automatically an
End(V tensor V) Delta-intertwiner. General divided-N rows and
large bands are not covered by a fixed bounded-band assertion.

## 4. The bounded-band Gaussian construction is genuinely positive

The interior theorem in Section5 of the main construction also
passes independently. Removing both cuts leaves a connected
internal graph. Any balanced fixed boundary offset has an integral
tree particular flow. Every other solution differs by an internal
cycle, with the same free transverse chords. For offsets fixed
independently of N, each original local position/transfer changes
by bounded integers. Actual proper factorial/Cartan ratios are
therefore finite products of known rational shifts. Their principal
symbols are units on the regular shape chart, with the original
common compact, peripheral, phase and half-density lines retained.

The two physical coordinates give a nondegenerate transverse
Hessian. The original Gaussian of that proper-ratio insertion has
the same marked action and a nonzero leading amplitude. Its value
is independent of a FIXED bounded particular-flow choice by the
exact transverse translation identity. An N-cycle is a finite
logarithmic-deck move and needs its additional period mark.
The explicit interior port/current identities consequently have
a canonical LOCAL cochain pushforward, not merely a dimension
count. Original support and endpoint rows remain their separate
relative summand; this theorem does not evaluate them.

The nearest-band principal ratios are also correct in the ACTUAL
balanced/factorial frame. Its canonical boundary form uses
p_new=(1-A)p_old. Holding inputs fixed and shifting outputs by
(p,q) changes the principal action by p Log p_cut+q Log p_e.
The cut value is one, giving
\[
             R_{(+1,-1),0}=p_e^{-1},\qquad
             R_{(-1,+1),0}=p_e.                    \tag{5}
\]
Internal tree contributions cancel by critical momentum matching.
Using the old momentum without its frame factor would change (5).

## 5. A physical two-parabolic chart and its sign target

In a common ACTUAL physical chart, take a normalized cut meridian
g_0=[[1,1],[0,1]], a trace-two meridian g_e=[[a,b],[c,d]],
h=a-d, and F=[[r,1-r],[s,-s]]. Then
\[
 P=F E_{11}F^{-1}
  =\begin{pmatrix}r&r(1-r)/s\\s&1-r\end{pmatrix},\quad
 k_e=\operatorname{Tr}(g_eP)
                 =d+hr+bs+c r(1-r)/s.
\]
Let A=1/(1+s), B=1/k_e, tau=r/s and
D=c+sh-2cr. Direct differentiation and trace/determinant identities
give
\[
 D^2=c^2+4cs(1-B^{-1}),\qquad
 \Omega_{cut}=\frac{d\log A\wedge d\log B}{BD}.     \tag{6}
\]
If c=0, trace2 and determinant1 force a=d=1, and B depends
only on s, contradicting an independent pair. Thus a rank-two
chart has c!=0. The quadratic discriminant is generically
nonsquare (its pole at B=0 is simple), and the deck is
r to 1+sh/c-r. It flips D and Omega. Ordinary field trace of
the coefficient1/(BD) is consequently ZERO.

The symmetric matrix Q=[[h/c,1],[1,0]] has determinant -1 and
satisfies g_0Q=Qg_0^t, g_eQ=Qg_e^t. Thus the same deck is
P to QP^tQ^-1. This is a bilinear transpose statement, not an
assertion of a positive Hermitian structure or an already proved
quantum-Weyl symmetry of the whole word.

In the moving cut frame the ACTUAL factorial momentum form is
\[
 g_{cut}=\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix},\quad
 g_e^{cur}=\begin{pmatrix}k&(1-k)p_e\\(k-1)/p_e&2-k\end{pmatrix}.
\]
If these are the displayed matrices in that same physical frame,
with c=Tr(g_cut g_e^cur)-2 fixed, put z=s(k-1). Then exactly
\[
 c=z(2-p_e-p_e^{-1}),\qquad D=-z(p_e-p_e^{-1}).
\]
One may also verify D=-Tr([g_0,g_e]P). On the regular z!=0,
p_e!=0 chart, the deck is precisely p_e to p_e^-1. Formula (5)
therefore gives a genuine actual LOCAL odd-band observable
\[
 R_{(+1,-1),0}-R_{(-1,+1),0}=D/z.
\]
Its product with (6) is the nonzero even density
dlog A wedge dlog B/(Bz). This does not say the original q=0
identity-cap source inserts that observable or selects that sign
cycle. That is a specified remaining source-parity test.

The physical dictionary is essential: in the existing marked
holonomy construction H_j=B_(minus,prefix)^-1 G_j B_(minus,prefix).
A developed meridian cannot be substituted for a physical Gauss
matrix solely because both have trace two. The conditional chart
consequence above requires the actual prefix/port adapter.

There is an alternative finite parity-moment test where a third
physical meridian clock is available in the SAME frame. For
g_f with entries a',b',c',d', h'=a'-d' and W=c'h-ch' nonzero,
\[
 r=\frac{c'k_e-c k_f-(c'd-cd')-(c'b-cb')s}{W}.       \tag{7}
\]
Thus D is a rational combination of three actual clock observables;
its moment can be inserted through the retained internal-edge
coupling, with no extra pivot. If the descended quadratic field is
F(D), Delta=D^2, and lambda=Tr((a_0+a_1D) times -), then
\[
                  \lambda(1/(BD))=\lambda(D)/(B\Delta).
                                                               \tag{8}
\]
The actual odd moment lambda(D), rather than a chosen field-trace
normalization, is the coefficient to test. Formula (7) has the
same physical-prefix qualification as (6).

## 6. The exact remaining selected-class square

Two physical cuts now give both external difference directions
and their complete finite matrix/source complex. The old
one-cut obstruction does not apply. Local transverse Gaussian
transport also has both physical base variables and the bounded
band currents just proved. These are genuine improvements.

The whole selected comparison still needs the original internal
finite head projections. In the known relative/Rees diagram their
actual maps are, with all head flags retained,
\[
                   P_t^{rel}(\sigma)
                         =e^{(\sigma-p/d)u}P_t.     \tag{9}
\]
Opening a second identity edge does not remove the remaining
internal projectors. A proposed whole geometric pushforward Gamma
must intertwine (9) and both endpoints, in addition to the actual
crossings and the selected two-cut tail/co-source. Its elementary
defect is the specifically typed expression
\[
           E_O=\Gamma_{out}O_{act,rel}
                                  -O_{geo,rel}\Gamma_{in}.
\]
For a word its residual is the finite telescoping sum
\[
 \sum_t O_{geo,>t}\,E_{O_t}\,O_{act,<t}.             \tag{10}
\]
The internal source equation (9), not a generic formal Morse
assertion, is a concrete remaining test. Its irregular factor
cannot be silently replaced by a regular vacuum. The exact whole
Fermat-trace source is one available explicit function for this
comparison, with its original norm, trace and power characters.

Equations (9)--(10) do not assert an obstruction to constructing
Gamma. They identify what the new external matrix/coherent map
does not yet prove. Extending it through these specified internal
maps and proving the selected sign/orientation would give the
desired whole source-class comparison; neither selected survival
nor volume growth follows just from local nonzero Gaussian bands.

## 7. The actual prefix correction passes, including the parity signs

The later
[prefix-adapted two-position proof](prefix_adapted_two_position_framing_cover.md)
passes independently. It resolves the physical-prefix qualification
in Section 5. For U=mu_j...mu_1 and V=mu_(j-1)...mu_1, the actual
second clock is k=ell_U/ell_V. With C=U-kV the correct density is

\[
       \Omega_{cut}=\frac{\ell_V}{BD}\,d\log A\wedge d\log B,
       \qquad D=\partial_\tau\ell_C.                         \tag{11}
\]

The Section 5 density with numerator one is a special chart, not a
formula for every physical internal edge. Direct quadratic root
summation gives

\[
 \operatorname{Tr}(\ell_V/D)
       =\frac{c_Vh_U-h_Vc_U}{(c_U-kc_V)^2}.                   \tag{12}
\]

It can be nonzero; the actual figure-eight prefix in the main note
has c_Vh_U-h_Vc_U=2u+1 for u squared plus u plus one equal to zero.
The claimed rational primitive of the resulting trace form also has
the correct sign. A nonzero field trace is not a selected period.

The signed triangular reconstruction gives exactly
beta=(-1)^j e_j and gamma=(-1)^j K_j f_j, because both triangular
prefix adapters cancel out of these off-diagonal entries. Thus

\[
 \beta=(-1)^j(k-M^{-1})p,\qquad
 \gamma=(-1)^{j+1}(k-M)/p.
\]

At M=1, Tr(JC) fixes beta-gamma and differentiation gives
D=s(beta+gamma). Hence the deck sends beta,gamma to -gamma,-beta,
and p to p inverse, with
D=(-1)^j s(k-1)(p-p inverse). This independently checks the parity
j in its nearest-band and density formulas. The generic-meridian
twisted reciprocal formula follows by using the actual cut meridian
entries M inverse minus k_0 and k_0 minus M in this same trace
equation; it also passes.

Finally the literal inverse signed prefix is
(q/M)^(j-1) product_(i<j) Q^(J_i). It is an actual finite diagonal
clock observable with its peripheral factor, not a postselected
scalar. Its principal symbol removes ell_V from (11). The note
correctly keeps its ordered crossing/current transport and does not
claim that it commutes through the whole word.

## 8. The finite identity cap has a marked orientation presentation

[The marked cap-cover identity](identity_cut_orientation_cover_and_marked_source.md)
now supplies an exact positive source comparison before any Gaussian:

\[
 F(\eta)\frac{d\eta}{N\eta}
     =[(\eta-\eta^{-1})F(\eta)]
                \frac{d(\eta+\eta^{-1})}
                     {N((\eta+\eta^{-1})^2-4)}.              \tag{13}
\]

The original cap marks eta=0, equivalently the preimage of u=infinity
with v/u tending to -1. Its exact residue has all finite negative
odd-band tails, with partial-sum endpoint (F_0-F_(-2K-2))/N.
The compensating measure and this endpoint prevent replacing the
original state by an arbitrary odd observable. The total form has no
new branch-point poles. No global tensor involution is assumed.

The principal prefix formula identifies eta=p inverse and gives
Omega_cut/ell_V=[(k-1)/(A_1-A_0)] dlog A wedge d eta/eta on its
regular coordinate chart, where A_0=c_U+s Tr U and A_1=c_V+s Tr V.
This checks the principal density and its full rational Jacobian.
Transporting the entire marked residue through the actual internal
projectors and transverse Gaussian remains the global comparison.

The new independent exact audit passes 21 literal actual signed braid
tensors, seven literal-unknot levels and all 8,771 port matrix units
at those levels, including their whole clocks and finite endpoints.
See the linked cap-cover note and its reproducible script/results.

The same note now records an important exact GEOMETRIC boundary check.
Its eta_geo=p inverse differs from the finite Fourier-band variable
eta_F. The relation eta_F p=1 is principal Fourier incidence, not an
ordinary source-coordinate change or a map of the cap cycle. In the
geometric relation u=p+p inverse, eta_geo=0 forces k to one and selects
D=A_0-A_1. If c_U-c_V is nonzero, the prefix root r and ell_V stay
finite. The full density multiplier ell_V(k-1)/(A_1-A_0) is O(eta),
so Omega_cut has zero logarithmic residue there. This does not identify
that boundary with the image of the original eta_F cap. For the actual
figure-eight prefix at s=1 the limiting data are r=-2 and
ell_V=2+3u_shape, with c_U-c_V=1 and A_0-A_1=3+u_shape.
If a proposed source transform assigns the cap to this geometric
boundary, a nonzero image needs its retained polar, endpoint or
escaping block amplitude; the geometric residue functional is
equation (19) of the cap-cover note. The finite identity (13)
does not by itself imply that an interior regular Gaussian density
has the original nonzero cap. This is a concrete remaining source
coefficient, rather than a choice of an odd cycle by hand.
