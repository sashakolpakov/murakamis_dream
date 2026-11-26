# The mixed rational word and the original collar representation

This note gives the exact representation equations behind the
mixed-word boundary phase. It uses the original rational tangle,
the original positive carrier, and the full ordered boundary
meridians. The outside piece has an explicit four-crossing Wirtinger
presentation. Keeping its original carrier and four interface arcs
identifies the complete source representation and then its geometric
deformation germ.

## 1. Propagating the actual through cap

Let \(z\) denote the trace of the first two through-cap
meridians. This notation differs by \(2\) from the lower
unipotent entry used in some of the earlier calculations.
The actual cap has ordered trace coordinates
\((z,2,4-z)\). In Newton clock and momentum coordinates,
resolve it by
\[
 q\longrightarrow1,\qquad
 v=\frac{(q-1)^2}{zq-q^2-1}.
 \tag{1}
\]
This retains the free parameter \(z\); substituting \(q=1\)
before the resolution would lose it.

The active positive crossing, inverse crossing and turn are
\[
\begin{split}
 R(x,v)&=\left(x+\frac{x-1}{v},-x(1+v)\right),\\
 R^{-1}(x,v)&=\left(\frac{xv}{v+1-x},-\frac{v+1}{x}\right),\\
 T(x,v)&=(x^{-1},v^{-1}).
\end{split} \tag{2}
\]
Their physical meaning and the ordered parabolic matrix
intertwiner are established in
[the original canonical-graph note](actual_newton_twist_canonical_graph.md)
and [the marked flag calculation](research_newton_crossing_marked_flags.md).
In particular, the inverse in (2) includes the denominator
\(v+1-x\).

Apply \(R,R,T,R^{-1},R^{-1},T\) to (1), in that order.
The successive regular values after the first two crossings are
\[
\begin{array}{c|cc}
\text{operation just completed}&\text{clock}&\text{momentum}\\ \hline
R^2&z-1&z-2\\
TR^2&(z-1)^{-1}&(z-2)^{-1}\\
R^{-1}TR^2&(z^2-3z+3)^{-1}&-(z-1)^2/(z-2)\\
R^{-2}TR^2&
 (z-1)/(z^3-5z^2+10z-7)&(z^2-3z+3)^2/(z-2)\\
TR^{-2}TR^2&
 (z^3-5z^2+10z-7)/(z-1)&(z-2)/(z^2-3z+3)^2.
\end{array} \tag{3}
\]
The first individual \(R\)-image can escape the Newton chart.
The cap matrices themselves are regular, so (3) is obtained
by the rational limit, not by assuming every intermediate
Newton clock remains finite.

Write the last row as \((E(z),V(z))\). Setting
\(X=(z-1)^{-1}\) and \(Y=E(z)\) gives
\[
 X^2Y-X=(1-X)^3,\qquad
 V(z)=-\frac{1-XY}{(Y-1)^2}. \tag{4}
\]
These are identities of rational functions. The map (3)
therefore describes the boundary of the actual rational word,
with its original through cap, for every regular nearby
representation.

## 2. Matching the deformed boundary leaf

For the original leaf let \(w=e^{iu}\), and use its ordered
geometric parameters \(E,T,R\). The leaf Legendre equations give
\[
 E=Y,\qquad
 T=\frac{wY+1}{Y+w},\qquad
 R=\frac{(Y+w)(wY+1)}{Y(w+1)^2}. \tag{5}
\]
Its Newton input momentum is the full flagged-matrix
dictionary
\[
 V_{\rm leaf}=\frac{1-R}{R}
       =-\frac{(Y-1)^2}{(Y+w)(Y+w^{-1})}. \tag{6}
\]
Thus \(V(z)=V_{\rm leaf}\), together with (4), is exactly
\[
\begin{split}
 X^2Y-X&=(1-X)^3,\\
 (1-XY)(Y+w)(Y+w^{-1})&=(Y-1)^4.
\end{split} \tag{7}
\]
These are the two critical equations of the full mixed
boundary source. This comparison is valid away from the
displayed denominators, all of which are nonzero at its
selected complete point.

Matching only a trace triple would be insufficient if the
boundary labels were unspecified. Here both sides use the
same ordered quadruple
\[
 (a,b,c,d)=(P_1^{-1},P_2^{-1},P_3^{-1},P_0^{-1}),\qquad
 dcba=1, \tag{8}
\]
of [the marked flag calculation](research_newton_crossing_marked_flags.md).
The rational-word operations are the actual Hurwitz maps on
that labelled boundary. The leaf dictionary includes a
simultaneous conjugacy of all four matrices. At an irreducible
point the ordered trace triple also determines the quadruple
up to conjugation, so the comparison extends across a
temporary singularity of a chosen Newton normalization.

## 3. The positive-carrier collar presentation

The original odd-collar face relations, before any coordinate
substitution, are
\[
 W_0^{-1}BW_2^{-1}A=1,\qquad
 W_2^{-1}BW_0^{-1}A=1,\qquad
 W_1^{-1}BW_3^{-1}A=1. \tag{9}
\]
Their ordered shaded pairing is the positive carrier
\(B:(Z,R,0)\mapsto(Z/E,\infty,1)\); the negative carrier
would use a different primitive meridian.

Choose the projection-chart tree edge \(W_0\) as the identity.
Put
\[
\begin{gathered}
 \mu=B,\quad L=W_2^{-1},\quad
 a=W_1^{-1},\quad b=W_2^{-1}W_1,\\
 c=W_3^{-1}W_2,\quad d=W_3.
\end{gathered} \tag{10}
\]
Eliminating \(A=W_2B^{-1}\) from (9) gives
\[
 dcba=1,\qquad L=ba,\qquad
 [\mu,L]=1,\qquad \mu c\mu^{-1}=a^{-1}. \tag{11}
\]
Eliminating \(b,c,d\) gives
\[
             \langle a,L,\mu\mid[\mu,L]=1\rangle
                         \cong \mathbb Z*\mathbb Z^2. \tag{12}
\]
This is the compressionbody group expected for the outside
crossing-circle piece. Its disk longitude is \(L\), and
its positive-carrier meridian is \(\mu\).

Here is a direct relative Wirtinger proof that these are all
relations, without treating completion maps as assembled white faces.
Use the original PD code (1) in the peripheral transport note.
The four oval crossings \(c_0,c_1,c_2,c_3\) are its rows
\(5,6,7,8\), with numbering starting at zero. Orient both
vertical strands from bottom to top and orient the oval
clockwise. Let \(g_j\) denote the Wirtinger meridian of arc \(j\).
Set
\[
 l=g_0=g_1,\quad r=g_9=g_{10},\quad
 p=g_2,\quad q=g_{11},\quad h=g_{17}=g_{16}=g_{15}.
\]
The complete list of oval crossing relations is
\[
\begin{array}{c|c|c}
\text{crossing}&\text{PD row}&\text{relation}\\ \hline
c_0&(1,16,2,17)&p=h^{-1}lh\\
c_1&(10,15,11,16)&q=h^{-1}rh\\
c_2&(14,9,15,10)&g_{14}=r^{-1}hr\\
c_3&(17,0,14,1)&h=l^{-1}g_{14}l.
\end{array} \tag{13}
\]
For example, at \(c_0\) the oval follows slots \(3\to1\),
and the left strand follows \(0\to2\). At \(c_2\), the
right strand follows \(1\to3\), and the oval follows
\(2\to0\). Reversing both over- and under-strand directions
retains the displayed Wirtinger conjugation. The two bottom
relations eliminate \(g_{14}\) and give exactly
\([h,rl]=1\). There are no further crossings in this open
outside piece.

The carrier is above this oval, not below it. Its PD row is
\((2,11,3,12)\). The positive crossing has lower slots
\((0,1)\) and upper slots \((3,2)\). Consequently the four
corners of the original rational tangle, in the original order
(lower left, lower right, upper right, upper left), lie on
arcs
\[
                         (12,3,9,0).
\]
The two upper corners use the original exterior closure arcs.
Thus its outwardly based meridians are
\[
 a=g_{12},\qquad b=g_3,\qquad c=g_9^{-1},\qquad d=g_0^{-1}.
 \tag{14}
\]
The carrier takes this pair downward into the oval's upper
pair. The original positive Hurwitz convention gives
\[
                 (p,q)=(a^{-1}ba,a). \tag{15}
\]
This is also the literal crossing relation \(a=g_{11}\),
\(g_2=a^{-1}g_3a\) in the recorded carrier row. It does not
move a crossing to the opposite side of the oval.

Combining (13)–(15), define the source-oriented meridian
and disk longitude by
\[
                       \mu=h^{-1},\qquad L=ba=rl. \tag{16}
\]
Then \([\mu,L]=1\), \(c=r^{-1}\), and
\(\mu c\mu^{-1}=a^{-1}\). Also \(d=l^{-1}=L^{-1}\mu^{-1}a\mu\).
These are precisely (11). The eliminations of the intermediate
arc generators are reversible, so the presentation is complete.
The curve \(h\) is an ordinary meridian of the original crossing
circle; \(\mu\) is its inverse. The curve \(rl\) is the boundary
of its twice-punctured disk, with each puncture traversed once.
It is the original preferred longitude, with no added meridian
or full twist. This establishes the primitive marking as well
as the abstract group (12).

There is a useful uniqueness statement that does not require
a metric. Once the ordered quadruple in (8) is fixed, a solution
\(\mu\) of (11) is unique in the projective group whenever
\(L\) and \(c\) do not commute. Indeed, the quotient of two
solutions centralizes both \(L\) and \(c\). At the complete
point \(L\) is a nonidentity parabolic, and the only translation
centralizing another parabolic with a different fixed point
is the identity. The same conclusion holds in a neighborhood
of that point. Hence a representation of this collar is
determined by its full irreducible boundary representation.

## 4. A general representation lemma

**Proposition 1.** Fix the positive-carrier outside piece just
described and any actual rational word on its four labelled
endpoints. On the regular irreducible locus, matching that
word's propagated cap representation with the original leaf
quadruple constructs a representation of the literal augmented
complement. If its complete base representation is geometric,
its small decorated family is the marked geometric deformation
germ, with the original leaf peripheral logarithms.

**Proof.** A rational tangle is a homeomorphic image of the
through tangle. Its complement group is free on the two
through-cap meridians, and its four boundary generators are
the transported cap generators. The original signed Hurwitz
maps and turns transport all four with their labels. Equation
(11) is the full outside-piece presentation. Matching the full
quadruple therefore permits van Kampen gluing, and the
uniqueness assertion above fixes its auxiliary generator.
If the resulting representation at the base point is the
complete holonomy of an actual positive ideal triangulation,
the proved marked gluing-germ theorem applies. Main meridians
and an auxiliary primitive longitude are local coordinates;
the leaf flag and its nonzero vertex differences persist
nearby. This identifies the whole representation family and
its peripheral logarithms with the geometric germ. Nothing
in this argument selects a quantum integration cycle or
proves a nonzero asymptotic coefficient. \(\square\)

## 5. Complete solutions and their exact cusp ratios

The disk longitude is \(L=ba\). At a complete geometric
representation it is parabolic. The two trace-two meridians
\(a,b\) have distinct fixed points, so \(\operatorname{tr}(ba)\)
cannot equal \(2\); it equals \(-2\).

For the word (3), direct substitution in the actual trace
function gives
\[
 A(z)+2
   =(z^2-5z+7)(z^3-3z^2+5z-2). \tag{17}
\]
None of these five roots is a pole of (3). Completeness of
the leaf gives
\[
 R=\frac{(E+1)^2}{4E},\qquad
 \tau(z)=\frac{\operatorname{trans}(L)}
                  {\operatorname{trans}(\mu)}
                         =-1-\frac1{E(z)}. \tag{18}
\]
The quadratic factor of (17) gives
\[
                       7\tau^2+20\tau+16=0,
\]
and its cubic factor gives
\[
                       17\tau^3+58\tau^2+72\tau+32=0.
 \tag{19}
\]
On the cubic factor,
\[
 E=2z^2-6z+9,\qquad
 E^3-7E^2+7E-17=0,\qquad
 z=\frac{E^2-8E+15}{8}. \tag{20}
\]
In particular the exact cusp ratio determines the entire
irreducible complete rational-word representation.

## 6. The geometric germ of the mixed word

The [peripheral transport certificate](research_mixed_two_crossing_peripheral_transport.md)
gives the original PD ratio
\[
                       \tau_{\rm PD}=1+\frac1{Y_*},
\]
where \(Y_*=1+2X_*+2X_*^2\) and \(X_*\) is the upper root of
\(X^3+2X^2+1\). The polynomial of \(\tau_{\rm PD}\) has
no common factor with either polynomial in (19); the
negative ratio is the selected root of the cubic in (19).

Every complete geometric representation of the original
diagram restricts to its actual rational cap family and
satisfies (17). The collar meridian and disk longitude are
ordinary primitive meridian and preferred-longitude curves.
Their discrepancy from the PD curves is therefore at most
an independent choice of orientations. Equations (18)–(19)
then force
\(\tau=-\tau_{\rm PD}\), selecting \(E=Y_*\) and the exact
cap parameter in (20). The uniqueness assertion after (12)
identifies the whole complete representation, including the
auxiliary generator.

Equations (5)–(7) therefore construct a holomorphic family
of representations of that same original group through its
complete holonomy. All main meridians remain parabolic.
The original peripheral logarithms are
\[
 U=-2\pi S'(u)-iu,\qquad V=2iu. \tag{21}
\]
The positive triangulation and the proved
[marked gluing-germ theorem](general_marked_multicusp_gluing_rigidity.md)
identify such a family with the actual geometric deformation:
main meridians and the auxiliary primitive longitude form
unramified local coordinates. This completes the marked-germ comparison needed for a
long final filling.

The irreducibility used here does not assume that the rational
tangle exterior injects on fundamental groups. If its two
cap meridians had a common fixed point, every transported
main meridian would share it. The nonidentity disk longitude
would then fix that point, and every commuting auxiliary
meridian would also preserve it. The complete holonomy would
be elementary, which is impossible for the positive finite-
volume structure already certified. Thus the actual complete
representation lies in the irreducible cap family. Every root
of the complete equation is regular in (3), so that argument
does not discard a possible geometric point at a chart pole.

## 7. A long final filling of the mixed word

**Corollary 2.** There is a finite integer \(C\) such that every
fixed odd signed \(c\) with \(|c|\ge C\) has the following
property. Close the original rational word
\(T(R^{-2}T(R^2))\) by the original final power \(R^c\), with
its original disk frame and reduced framing convention.
The resulting knot \(K_c\) is hyperbolic and its original
Kashaev invariant satisfies
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
          \log|\langle K_c\rangle_N|
                  =\operatorname{Vol}(S^3\setminus K_c).
 \tag{22}
\]
The mirror statement follows by conjugating the full source
and reversing every crossing sign.

**Proof.** The actual boundary source theorem gives
\(Z_N(u)=A(u)e^{NS(u)}(1+O(N^{-1}))\), with nonzero holomorphic
amplitude, \(-\Re S''(0)>0\), and the full real and complex-strip
bounds. The scalar closing proof in Section 7 of
[the fixed-domain theorem](research_fixed_domain_long_power_turns.md)
uses only these hypotheses. Applied to the original exact
trace
\[
                          \phi_N(R^cZ_N),
\]
it gives a nonzero leading term
\[
 \Omega_N N^{3/2}D_c e^{N\mathcal V_c}(1+O_c(N^{-1})),
 \qquad |\Omega_N|=1,\quad D_c\ne0,
 \tag{23}
\]
where
\[
 \mathcal V_c=S(u_c)+\frac{ic}{4\pi}u_c^2-iu_c,\qquad
 S'(u_c)+\frac{ic}{2\pi}u_c-i=0.
 \tag{24}
\]
Its charge path is obtained by replacing the final \(i\) by
\(i\lambda\), \(0\le\lambda\le1\). For sufficiently large
\(|c|\) it stays in the marked geometric disk proved above,
and \(\Im u_\lambda<0\) for \(\lambda>0\).

The retained carrier is \(\eta=1\). Put \(p=(1-c)/2\), which
is integral because \(c\) is odd. Equation (21) gives the
original primitive filling equation
\[
 U+pV=-2\pi\left(S'(u)+\frac{ic}{2\pi}u\right)
                                  =-2\pi i\lambda.
 \tag{25}
\]
Its core has positive length \(-2\Im u_\lambda\). This is the
usual local completion of the marked positive gluing under a
long primitive filling; at \(\lambda=1\) the meridian angle
is \(2\pi\). The initial volume is already fixed absolutely:
\[
                   \operatorname{Vol}(M)=2\pi\Re S(0).
\]
Schläfli's formula along (25) then gives
\[
                \operatorname{Vol}(M(\mu+p\lambda))
                                    =2\pi\Re\mathcal V_c.
 \tag{26}
\]
There is no unspecified additive volume constant.

Both inner powers are even. The mixed pendant therefore has
the through pairing of its four endpoints. In the specified
braid closure a final odd crossing power joins the two main
strands into one component; an even power would leave two.
Thus the filling in (26) is the stated knot complement.
The original reduced zero-framed invariant differs from
(23) only by the prescribed unit framing factor, so (22)
follows. \(\square\)

The threshold is fixed for this actual boundary piece; it is
independent of the chosen final signed \(c\). This corollary
settles the infinite family with the mixed short pair held
fixed and the last twist tending through all sufficiently
large odd values. It does not, by itself, cover arbitrary
adjacent short regions in a larger circle tree.

## 8. Exact reproduction

Run the representation calculation with

    .venv/bin/python experiments/verify_mixed_word_collar_representation.py

For an independent report use

    .venv/bin/python experiments/verify_mixed_word_collar_representation.py \
      --output /tmp/mixed-word-collar-review.json

The [verifier](../experiments/verify_mixed_word_collar_representation.py)
checks the literal PD endpoint and strand paths, the resolved cap
word, the deformed leaf dictionary, all four boundary matrices,
the full positive-carrier relations, the complete cusp polynomials
and the recovery of the cap parameter from the cusp ratio.
Its [saved report](../repro/results/research-mixed-word-collar-representation.json)
records the script and original diagram fixture hashes.
The separate peripheral verifier cited in Section 6 checks the
actual original curves and the complete positive triangulation.



