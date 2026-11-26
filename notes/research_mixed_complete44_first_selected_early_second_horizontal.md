# A complete selected-first horizontal over the early second interval

Private written deduction, 11 November 2026. The first Fourier term
remains selected at height \(1/100\). Its entire horizontal interval
\([1/10,9/20]+i/100\), multiplied by the complete next own-four
kernel, has a strict bound when the second coordinate moves left
from \(11/50\) to \(1/10\) at its actual negative height.

Both conditional sums and the whole cap are retained. The argument
uses the old selected pair comparisons only at the face \(q=11/50\).
All changes to their positive incoming-height source are proved
below. The remaining first-coordinate joins and real arcs, and
therefore the whole selected first coefficient, are not concluded.

## 1. Exact source, allocations and old-face comparison

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\). Keep its original coupled reference, ordinary color,
private indices, phases and logarithmic lifts. Write
\[
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad H=1/100,
\]
\[
 a=x+iH,\quad 1/10\le x\le9/20,\qquad
 y=q+ic_2,\quad q\in E,\qquad z=u+ic_3,\quad u\in P .
 \tag{1}
\]
Here \(c_2,c_3,h_s,h_t\in[-.102,-.001]\), where \(h_s,h_t\)
are the actual ordinary private heights at vertices two and three.
The actual cap private height lies in \([-.051,-.019]\).
The weaker bound \([-.108,0]\) is used for some index estimates.
At \(m=4\) the third vertex is ordinary and its following leg
is attached, with the original incidence.

For \(r_N=e^{-2\pi i/N}\), put
\[
 P_j=(r_N;r_N)_j,\quad p_j(V)=(r_NV;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\]
Retain
\[
 U_{1,N}(w,X)=\sum_{i<N}H_N(w,r_N^{-i})\,p_i(X)/P_i^2,\qquad
 C_{1,N}(X,Y)=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3 .
 \tag{2}
\]
The density to be bounded is exactly
\[
 \mathscr K_N^+
 =U_{1,N}(w,X)d_N(X)X^{-N}C_{1,N}(X,Y)
                         d_N(Y)C_{1,N}(Y,Z).
 \tag{3}
\]
The outgoing allocation is \(|d_N(Z)|^{1/2}\). There is no
selected monomial at \(Y\). The first extraction, if this
horizontal is integrated, retains its single positive density
\(N\,da\).

Let \(Q(s;b,c)=g(s+b)+g(s+c)-3g(s)-g(b)-g(c)+2\pi ibs\),
where \(g=J+\pi i(v-v^2)/2\) has its original absolute constant.
Let \(\Lambda_{123}(z)\) be the original three-factor affine
action:
\[
 \Lambda_{123}(z)=
 \Re\{L_1(r_1)+\phi_2(r_1,r_2)+\phi_3(r_2,r_3)
                    +\partial_2\phi_3(r_2,r_3)(z-r_3)\}.
 \tag{4}
\]
Thus its absolute constant is the stationary value of
\(\Psi+Q(s;a,y)+Q(t;y,z)-g(a)-g(y)-g(z)/2\).

**Theorem.** For every \(\tau>0\), a sufficiently small fixed
ordinary-color disk about \(-2\), both level parities and all
sufficiently large \(N\) satisfy
\[
 |\mathscr K_N^+|\,|d_N(Z)|^{1/2}
 \le C_\tau N^{B_\tau}
             e^{N\{\Lambda_{123}(z)-1/2000+\tau\}}
 \quad\hbox{on (1)}.
 \tag{5}
\]
In particular one may take a fixed gap \(1/4000\).
Fixed ordinary-color derivatives obey the same rate on a smaller
disk. Integration over any fixed subinterval of the horizontal
in (1), with its original \(N\,da\), changes only polynomial
factors.

Here are the precise old-face inputs. Put \(q_0=11/50\). For
\(x\in[1/10,q_0]\), the complete early selected-four source,
equations (27) and (37), pays every cap main, cut, alias and true
end against each first ordinary main or real cut at \(q=q_0\).
For \(x\in[q_0,9/20]\), Sections 2--3 of the complete selected
four/four product do the same. Its finite reduction bounds the
literal true ends by the same cap main profile. These are
profile comparisons before summation, not consequences of a
small signed finite kernel.

Denote any of these controlling cap rates by \(A_i(x)\).
The full first selected polynomial has the two upper rates
\[
 W_{\rm fac}(x)=-\Re g(a)-2\pi H,\qquad W_{\rm force}(x)=0.
 \tag{6}
\]
For either one, every old-face first profile has
\[
 A_i(x)+\Re Q(s;a,q_0+ic_2)-\tfrac12\Re g(q_0+ic_2)
          +W_\nu(x)\le\Lambda_{12}(q_0)-1/2000 .
 \tag{7}
\]
The profile \(s\) is on its whole original main or at \(1/8,1/2\).
The actual next own-four main, real cuts and last carrier have
their ordinary supporting bounds at this face. The two shared
halfweights give \(-g(y)\); the exact original marginal
cancellation makes the sum of the two affine planes (4).
Consequently, at \(q_0\),
\[
 A_i+W_\nu+\Re\{Q(s;a,y)+Q(t;y,z)-g(y)-g(z)/2\}
                   \le\Lambda_{123}(z)-1/2000
 \tag{8}
\]
for every pair of main/real-cut profiles. Replacing the second
profile by its literal last carrier \(\delta_y=-2\pi c_2\)
also satisfies (8), by the original typed last-row comparison.
Only its strict sign is used. Every \(A_i,W_\nu\) is independent
of \(q\), which is essential to the transports below.

## 2. Clipping the first main at positive incoming height

Put \(T=e^{-2\pi H}\). The elementary inequality
\[
 \log(16/15)>2/31>\pi/50
 \quad\hbox{gives}\quad 15/16<T<1 .
 \tag{9}
\]
For \(v\in[1/8,1/6]\), \(s=v+ih_s\), write
\(\rho=e^{2\pi h_s}\in[1/2,1]\) and \(R=e^{2\pi c_2}\in[1/2,1]\).
The exact folded force is
\[
 e^{\Re Q_s}=
 \frac{|T-\rho e^{-2\pi i(x+v)}|
       |1-R\rho e^{-2\pi i(q+v)}|}
      {|1-\rho e^{-2\pi iv}|^3}.
 \tag{10}
\]
Let \(c=\cos(2\pi v)\) and \(d=\cos(2\pi(v+1/10))\).
For \(x\in[.1,.45]\), the incoming shifted cosine is at most
\(d\). The second modulus is at least \(\sin(2\pi v)\):
before its angle reaches \(\pi/2\) use radial minimization and
increasing sine; afterwards the modulus is at least one.
Also \(d<1/6\).

The old elementary pentagon bounds give
\[
 d<\tfrac{13}{16}c-\tfrac7{12}\sqrt{1-c^2}.
 \tag{11}
\]
In particular, if \(c\le3/5\), then \(d<1/48\) and
\(1-c^2\ge16/25\). If \(c\ge3/5\), retain
\(1-c^2\ge1/2\). Radial minimization in the first factor is
at the lower endpoints of \(T,\rho\), since
\(T-\rho d>0\) and \(\rho-Td>0\).

The following explicit estimates prove the squared numerator
in (10) exceeds the cube of its own squared modulus.

* If \(c\ge3/5\) and \(\rho\le3/4\), the own square is at most
  \(53/80<2/3\), whereas the first numerator square is at least
  \(249/256\). Thus the squared numerator exceeds
  \(249/512>8/27\).
* If \(c\ge3/5\) and \(\rho\ge3/4\), the own square is at most
  \(4/5\), and the first numerator square is at least
  \(309/256\). The product exceeds \(309/512>(4/5)^3\).
* If \(c\le3/5\) and \(\rho\le3/4\), the own square is at most
  \(13/16\), and the first numerator square is at least
  \(71/64\). The product is at least \(71/100>(13/16)^3\).
* If \(c\le3/5\) and \(3/4\le\rho\le7/8\), those bounds are
  \(57/64\) and \(723/512\). The product exceeds
  \(723/800>(57/64)^3\).
* If \(c\le3/5\) and \(\rho\ge7/8\), the own square is at most
  one and the first numerator square is at least
  \(1649/1024>8/5\). Their product exceeds \(128/125>1\).

The own-square bounds use convexity in \(\rho\); hence it
suffices to check the stated radial endpoints. The first-factor
bounds are direct substitutions in \(T^2+\rho^2-2T\rho d\).
All comparisons are rational. Thus \(\Re Q_s>0\), proving
the upward clipping to \(v=1/6\).

For \(5/12\le v\le1/2\), both numerator moduli in (10) are
at most \(1+\rho\), because \(T,R\le1\). The own square is at
least \(D_\rho=1+\rho^2+12\rho/7\), and
\[
 D_\rho-\tfrac75(1+\rho)
       =\rho^2+\tfrac{11}{35}\rho-\tfrac25\ge1/140.
 \tag{12}
\]
The squared force is less than
\((1+\rho)^4/D_\rho^3<(1+\rho)(5/7)^3\le250/343<1\).
Every first main profile may therefore be increased to one with
\[
                         1/6\le s_R\le5/12 .
 \tag{13}
\]
The next own-four low-main clipping to \(t_R\ge1/6\) is
unchanged: its incoming height and outgoing height remain
negative. These clippings apply with every cap, weight and
other profile held fixed.

## 3. All main and real-cut pairs transport to the old face

Differentiation with the next chirp retained gives
\[
 \exp\partial_q\Re\{Q(s;a,y)+Q(t;y,z)-g(y)\}
 =
 \frac{|1-R\rho_s e^{-2\pi i(q+s_R)}|
       |T_t-R e^{-2\pi i(q+t_R)}|}
      {|1-R e^{-2\pi iq}|^3}.
 \tag{14}
\]
Here \(\rho_s=e^{2\pi\Im s}\) is in \([1/2,1]\), or is one
at a real first cut, and \(T_t=e^{-2\pi\Im t}\ge1\), or
is one at a real next cut. Neither the first incoming height
nor the cap enters this derivative.

On \([.1,.2]\), equations (19)--(22) and the explicit
real-face variant following (23) in the joint lower-left profile
proof apply directly to (14), using (13) and the next clipping.
They prove a strictly positive derivative for every main/cut
pair. Their weaker lower bound \(T_t>13/20\) is satisfied.

On \([.2,.22]\), retain
\[
 D=1+R^2-\tfrac9{25}R,\quad
 U=1+\tfrac14R^2+\tfrac{13}{20}R,\quad
 V=1+R^2+\tfrac9{25}R .
 \tag{15}
\]
For a clipped first main, its numerator square is at least \(U\).
For a next main or real cut, its square is at least \(V\):
its real index is at least \(1/8\), and the largest shifted
cosine is at most \(-\cos(2\pi q)<-9/50\).
Equations (25)--(26) of the same source prove \(UV>D^3\).
For the first real low cut, equations (27)--(29) prove the
corresponding positive product with every next main or cut;
again the present \(T_t\ge1\) only improves that proof.

The first real half is handled directly, without moving it to
a negative index height. Its numerator square is at least \(V\);
so is the second numerator square. On \(1/2\le R\le1\),
\[
 V-\tfrac{13}{10}D
 =-\tfrac3{10}(1+R^2)+\tfrac{207}{250}R>0,\qquad
 D\le41/25<169/100 .
 \tag{16}
\]
The first polynomial is concave with positive endpoint values
\(39/1000\) and \(57/250\). Consequently \(V^2>D^3\).
This proves positive transport of every main/cut pair through
the whole interval \(E\), up to \(q_0\).

After clipping, the endpoint profile at \(q_0\) is still one
of the profiles permitted by (8). Integrate the positive
derivative before taking any index maximum. Equation (8)
therefore holds on all of \(E\).

## 4. The next last carrier

The first high block will need only its half profile. The next
high block still has both its half and last alternatives.
For its last carrier \(\delta_y=-\log R\), the first-profile
derivative is exactly
\[
 \partial_q\{\Re Q(s;a,y)-\Re g(y)+\delta_y\}
 =\log|1-R\rho_s e^{-2\pi i(q+s_R)}|
                        -2\log|1-R e^{-2\pi iq}|.
 \tag{17}
\]
If \(R\le7/10\), Section 2 of the next-four last-row proof
shows that this is positive for a clipped first main or
its real low cut. That calculation is independent of \(a\);
the present clippings have been proved in Section 2.

For the first real half the numerator square is
\(1+R^2+2R\cos(2\pi q)\). On \([.1,.2]\) it exceeds
\(1+R^2/4+R/10\), the main lower bound in that proof.
On \([.2,.22]\) it exceeds \(1+R^2/4+13R/20\), since
\[
 \tfrac34R^2-\tfrac{29}{100}R
       \ge R(3/8-29/100)>0 .
 \tag{18}
\]
The same positive transport therefore holds for this real
half without a vertical comparison. The old-face last
comparison in (8) pays all these profiles.

If \(R\ge7/10\), Section 3 of that source proves at the
same targets
\[
 E_1(1/8;y,z)>\delta_y+1/1100 .
 \tag{19}
\]
Its proof uses only the unchanged next output in \(P\) at
negative height. Section 3 has already paid every first profile
paired with that next real cut. Thus (19) pays every remaining
next-last pair. No first-last alternative is introduced.

## 5. All first conditional finite currents at the changed height

The exact physical partition is
\[
 0\le j\le\lfloor N/8\rfloor,\quad
 \lfloor N/8\rfloor+1\le j<\lceil N/2\rceil,\quad
 \lceil N/2\rceil\le j<N .
 \tag{20}
\]
We give the new positive-height checks needed for its first
factor. The next factor's complete lower-left inventory is
unchanged.

For a low physical row \(0<v\le1/8\), its force is
\[
 \exp E_1'(v;a,y)=
 \frac{|T-e^{-2\pi i(x+v)}|
       |1-R e^{-2\pi i(q+v)}|}
      {(2\sin\pi v)^3}.
 \tag{21}
\]
The second modulus is at least \(\sin(2\pi v)\).
For \(v\le1/10\), the first is larger than \(4/7\):
when its shifted cosine is positive, radial minimization and
\(x+v\ge1/10\) give \(\sin(\pi/5)>4/7\); otherwise it
is at least one. Since
\((2\sin\pi v)^2<2/5\) and \(\cos\pi v>9/10\),
(21) is larger than \(9/7\).
For the sine witness,
\(\sin^2(\pi/5)=(5-\sqrt5)/8>11/32>16/49\), using
\(\sqrt5<9/4\). The denominator bound follows from
\((\pi/5)^2<(22/35)^2<2/5\).
For \(1/10\le v\le1/8\), the shifted cosine is at most
\(\cos(2\pi/5)<1/3\). Equations (9) then give
\[
 |T-e^{-2\pi i(x+v)}|^2
 >1+225/256-5/8>1 .
 \tag{22}
\]
The force is larger than \((9/10)/(3/5)=3/2\).
Thus the whole positive low block reduces to its real cut.
The uniform original factorial estimate includes \(j=0\)
and both rounded endpoint parities.

For the middle sum keep its original exact interpolant
\[
 e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                       E_N(a)E_N(y)E_N(s)^3 ,
 \tag{23}
\]
and half-grid cuts tending to \(1/8,1/2\). Use the fixed
lower and upper heights \(-1/5,4\). All shifted real parts
are strictly in \((0,1)\), including \(x+s_R\le.95\).
These contours are in the exact factorial theorem's regular
finite-height domain.

Write \(\mathcal A(v,h)=\arg(1-e^{2\pi h-2\pi iv})\) on
the original strip lift. The imaginary index derivative is
\[
 I=\mathcal A(x+v,H+\sigma)+\mathcal A(q+v,c_2+\sigma)
                      -3\mathcal A(v,\sigma)+2\pi x .
 \tag{24}
\]
The standard radial argument inequalities give, on
\(1/8\le v\le1/2\),
\[
 I<29\pi/20\quad\hbox{at every height},\qquad
 I>-37\pi/40\quad(\sigma\le0).
 \tag{25}
\]
For clarity, for the upper bound, if both shifted parts are
below one half use \(2-4v-2q\le13/10\). If only the outgoing
one is below, use \(1-2v-2q+2x\le29/20\); if only the incoming
one is below, use \(1-2v\le3/4\); if neither is below, use
\(2x\le9/10\). For the lower bound below zero use the full
strip lower bounds for both shifted arguments and
\(\mathcal A(v,\sigma)\le\pi(1/2-v)\). The corresponding
four lower bounds are
\[
 -3/2+3v+2x,\quad -1/2+v,\quad
 -1/2+v+2x-2q,\quad 1/2-v-2q .
 \tag{26}
\]
Their common lower bound is \(-37/40\).

Above zero the outgoing argument obeys equation (10) of the
complete-current source:
\[
 \mathcal A(v+q,\sigma+c_2)
 \ge B-\pi/4-\pi(1+\sqrt2)q,\quad
 B=\mathcal A(v,\sigma)\le\pi(1-2v).
 \tag{27}
\]
If \(v+x\ge1/2\), this yields
\(I/\pi\ge-5/4+2v-(1+\sqrt2)q>-537/350\).
If \(v+x<1/2\), the positive incoming height permits
\(\mathcal A(v+x,\sigma+H)\ge\pi(1/2-v-x)\), giving
\[
 I/\pi\ge-7/4+3v+x-(1+\sqrt2)q>-2533/1400>-2 .
 \tag{28}
\]
Here \(\sqrt2<10/7\) suffices. Thus every weighted vertical
half decreases away from its real cut. Integrating (25)--(28)
with the original sampling penalties gives
\[
 \Re Q(v-i/5)-2\pi/5
       <\Re Q(v+ih_s)-11\pi/100,
\]
\[
 \Re Q(v+4i)-8\pi
       <\Re Q(v+ih_s)-3\pi/5 .
 \tag{29}
\]
For the second inequality the upper cost is bounded by
\((37/40)(27/250)+4(2533/1400)\), which is less than \(37/5\).

It remains to keep both zero-mode joins from \(h_s\) to zero.
Put \(C(v,\sigma)=\Re\cot\pi(v+i\sigma)\).
On these joins \(\cosh(2\pi\sigma)<5/4\), while
\(\cos(2\pi v)\le1/\sqrt2<3/4\). Hence
\[
 C(v,\sigma)>\tfrac12\cot(\pi v)\quad(v<1/2).
 \tag{30}
\]
The outgoing shifted positive cotangent is at most \(C(v,\sigma)\),
because \(c_2<0\); its angular monotonicity is the original
negative-join proof. The incoming shifted cotangent, if positive,
is at most \(\cot\pi(v+x)<\cot\pi v<2C(v,\sigma)\),
irrespective of the sign of \(\sigma+H\). If either shifted
cotangent is negative, its omission only improves the comparison.
Thus
\[
 3C(v,\sigma)-C(v+x,\sigma+H)-C(v+q,\sigma+c_2)>0 .
 \tag{31}
\]
At the half cut the own term is zero and both shifted terms
are negative. The real index Hessian is negative, so the
real rate is vertically convex. Each unweighted join is
bounded by its two already paid endpoint profiles.

The exact residue decomposition therefore retains its \(+N\)
zero mode, two horizontal aliases, four weighted vertical halves
and two unweighted joins. Equations (25)--(31) pay them all
by the first main or real-cut profiles at the same \(q\).
The original half-grid \(O(1/N)\) displacements cost only
the standard source allowance.

Finally the first high block has exactly zero reflected drift:
\[
             2\pi\{(-H)_++(c_2)_+\}=0 .
 \tag{32}
\]
The all-angle high-row theorem applies to every present pair
of real angles in \((0,1/2)\), and bounds every row from
\(\lceil N/2\rceil\) through \(N-1\) by the continuous
half-row rate. No literal half-row value is divided out.

## 6. Complete product and scope

The next own-four kernel has the unchanged actual negative
incoming and outgoing heights. The low-physical proof, complete
lower-left current proof and own-four upper-row proof therefore
reduce it, with every original index and current, to its main,
real-low, real-half and literal last profiles. The printed
first-three source restrictions of those notes are not being
used for the first kernel: Section 5 supplies its changed
positive-height proof explicitly.

The complete cap envelope is independent of \(q\).
For \(x\le.22\) it is the six-profile envelope of the early
selected-four theorem, including its separate true-end rate.
For \(x\ge.22\) it is the original finite reduction's five
profiles, with the literal true ends already dominated by its
main profile. Their original cap joins, aliases, physical
tails and coherent endpoint coefficients have not changed.
Sections 3--4 pay every product of this envelope, either
first weight rate (6), a first main/cut profile, and any
next controlling profile.

On the compact negative second strip \(E+ic_2\), the complete
Fourier polynomial has upper rate \(-\Re g(y)\), including
its forcing. The outgoing allocation has rate \(-\Re g(z)/2\).
Their two incidences at \(Y\), and the one whole selected
factor at \(X\), are exactly the weights in (3).

Apply the two complete conditional reductions successively,
holding every outside factor fixed. There are finitely many
currents and at most \(N\) rows per physical block. Their
path lengths, \(+N\) residue densities, symbols and roundings
cost only polynomial factors and an arbitrarily small common
rate tolerance. The old-face gap \(1/2000\) survives the
nonincreasing transports, proving (5). The original cap
color disk and Cauchy's formula give the derivative assertion.
Both parity conventions and every zero of a numerator or
Fourier polynomial are retained without division.

This proves a complete finite-source estimate on the entire
specified selected first horizontal. It does not yet pay its
vertical connection at \(x=1/10\), its right height reset or
the complementary real arcs for the early second targets.
It consequently does not estimate the whole selected first
coefficient, the full \(R_{44,N}\), or the complete second
period. No new whole-word or filling conclusion is inferred.

## Direct source versions

The directly used implications are: the complete cap envelope and
every selected old-face profile in the first three sources; the
shared-coordinate rational transport, unchanged next low/current/
high/last inventory in the following five; the exact sign-class
high-row theorem; the original next ordinary plane and incidence;
the two full Fourier upper alternatives; the original finite
factorial interpolation; and the literal first-prefix normalization.
All have been read with these specific domains and allocations.

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_selected_four_four_full_product.md | 4fadefa2aa2ab731da1c1557aeec77113e2bbd5d491c7fd104011b24766a248d |
| research_mixed_selected_four_four_finite_reduction.md | d018c6ad4dd78e6a6c7ac649f0d5d8443b649f1f01d9c6acde586697da1da4e5 |
| research_mixed_next_lower_left_joint_main_profiles.md | 07844539d1ba13eadeba216be1f0888da9bbf43fc42e4e946f57199601289f3f |
| research_mixed_next_lower_left_low_physical_blocks.md | cd57a6112faab45b6737c3e154730029807a41b627ae1b7618d635361ca2485c |
| research_mixed_next_lower_left_complete_currents.md | 5d784371488e491be733f475f7f400df5b6230f6083e6e965b0fedfccbdc1d1a |
| research_mixed_next_lower_left_own_four_upper_rows.md | e67a0349acb90ced3c8c24d212388ec6f14237ce0935341a8243a18a849293f4 |
| research_mixed_next_lower_left_next_four_last_row.md | ac8bd37f1b7d775e57d51f33fcf455eb38405f62b442c9605202642c2899c641 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |

Author full written proof readback and all thirteen direct-source
implication reads and binding checks are complete. Independent full
proof/direct-source review is required before adoption. No
mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source change is used.
