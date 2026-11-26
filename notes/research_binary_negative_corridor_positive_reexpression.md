# A positive geometric presentation for negative chains of twos and threes

A negative chain made from powers minus two and minus three, with
power minus two at both ends, has an exact marked replacement by a
positive chain whose magnitudes are at least three. One positive
crossing remains at each outside boundary. The established geometric
theorem therefore gives a positive decomposition of the same partially
filled exterior, without assuming positivity of its old cells.

There is also an exact identity in the full original quantum algebra.
It gives another finite presentation of the same source. When the
runs of twos satisfy the bounds in Section 6, the established
long-power theorem applies to the replacement. This gives a full
pendant boundary asymptotic and, after a sufficiently long closing
twist, the volume conjecture for the resulting knot. The argument
does not require identifying stationary points in the old presentation.

## 1. The complementary continued fraction

Write the negative magnitudes as
\[
 \mathbf b=(2^{r_0},3,2^{r_1},3,\ldots,3,2^{r_k}),
 \qquad r_0,r_k\ge1,\quad r_1,\ldots,r_{k-1}\ge0.
 \tag{1}
\]
Here \(k\) counts the threes, \(2^r\) denotes a string of \(r\) twos,
and \(m=k+\sum r_j\) is the path length. Adjacent threes are allowed.
If there are no threes, write \(\mathbf b=(2^m)\). Set
\[
 \mathbf c=
 \begin{cases}
 (m+1),&k=0,\\
 (r_0+2,r_1+3,\ldots,r_{k-1}+3,r_k+2),&k\ge1.
 \end{cases}
 \tag{2}
\]
There are \(\ell=k+1\) complementary entries. All are at least three,
except for the single original vertex \(\mathbf b=(2)\), whose
complement is \((2)\).
When \(k=1\), there are no middle entries in the second line of (2).

**Lemma 1.** For the negative continued fraction
\[
 \alpha=[b_1,\ldots,b_m]_-
   =b_1-\frac1{b_2-\dfrac1{\cdots-1/b_m}},
\]
one has
\[
                   \alpha/(\alpha-1)=[\mathbf c]_-.
 \tag{3}
\]

**Proof.** If a tail has value \(\beta>1\) and complementary value
\(d=\beta/(\beta-1)\), then
\[
 \frac{2-1/\beta}{(2-1/\beta)-1}=d+1,\qquad
 \frac{3-1/\beta}{(3-1/\beta)-1}=2-\frac1{d+1}.
 \tag{4}
\]
Prepending a two increments the first complementary coefficient.
Prepending a three inserts a two and increments the previous first
coefficient. The last two has complement two. Induction from the
right gives (2). \(\square\)

Examples are \((2,3,2)\mapsto(3,3)\),
\((2,3,3,2)\mapsto(3,3,3)\), and
\((2,2,3,2,2)\mapsto(4,4)\).
The proof holds at every length. The arithmetic is the elementary
complementary continued-fraction operation; no novelty is claimed
for it.

## 2. Both outside attachments and their markings

Use the original crossing \(R\), clockwise turn \(T\), and their
supported affine pillowcase lifts
\[
 \widetilde R^{\,n}(x,y)=(x+ny+n/2,y),\qquad
 \widetilde T(x,y)=(-y,x+1/2).
 \tag{5}
\]
Their linear parts are
\[
 A_n=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
These are the actual maps proved in
[the marked degree-two moves](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_marked_degree_two_tangle_moves.md).
Put
\[
 W_-=TR^{-b_1}T\cdots TR^{-b_m}T,\qquad
 W_+=TR^{c_1}T\cdots TR^{c_\ell}T.
 \tag{6}
\]

**Proposition 2.** For every attached tangle \(F\), there is a specified
proper half-turn \(H\), possibly the identity, such that
\[
                      W_-(F)\simeq R\,W_+(R\,H(F)).
 \tag{7}
\]
Both boundaries remain present. The isotopy carries all marks,
outside branches and ribbons.

**Proof.** After its deck sign, the negative word has matrix
\[
 G=\begin{pmatrix}A&B\\C&D\end{pmatrix},
 \quad 0<A,D<C,\quad AD-BC=1,\quad C/A=\alpha,
 \tag{8}
\]
by the [rational normal-form theorem](research_definite_rational_corridor_normal_form.md).
Conjugate by \(\operatorname{diag}(1,-1)\) and take a deck sign.
The result is
\[
                    \begin{pmatrix}-A&B\\C&-D\end{pmatrix}.
\]
Its two integral normalizing twists are minus one; its normalized
diagonals are \(C-A,C-D\). The negative continued fraction is
\(C/(C-A)=\alpha/(\alpha-1)\), which Lemma 1 identifies as
\(\mathbf c\). Mirror this complete matrix identity back to obtain
\[
 S A_{-b_1}S\cdots A_{-b_m}S
     =A_1 S A_{c_1}S\cdots A_{c_\ell}S A_1
                    \quad\text{in }\mathrm{PSL}_2(\mathbb Z).
 \tag{9}
\]
Thus the comparison is of full two-boundary maps, not just slopes.

To specify \(H\), let \(B=R W_+R\), compute the actual affine maps
using (5), and write
\[
 \widetilde B^{-1}\widetilde W_-(z)=\epsilon z+v,
 \quad \epsilon\in\{1,-1\},\quad
 \delta=\epsilon v\bmod\mathbb Z^2.
 \tag{10}
\]
The retained proper rotation is
\[
\begin{array}{c|cccc}
\delta&(0,0)&(1/2,0)&(0,1/2)&(1/2,1/2)\\ \hline
H&1&\rho&K&T^2.
\end{array}
 \tag{11}
\]
This is a finite integer and half-integer calculation for any word.
The supported collar isotopy proves (7), with this rotation still
acting on \(F\). \(\square\)

For a pendant chain with through tangle \(I\), the identity is
\[
 TR^{-b_1}T\cdots TR^{-b_m}(I)
       \simeq R\,TR^{c_1}T\cdots TR^{c_\ell}(I).
 \tag{12}
\]
The relative linear map of the two sides, acting on the right, is
\[
             S A_1S^{-1}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}
 \tag{13}
\]
up to the deck sign. The actual turn-and-cap isotopy of the normal-form
theorem shows that it fixes \(I\); the remaining half-lattice
translation is a proper half-turn of \(I\) and also fixes the cap.
This does not erase \(H\) on an arbitrary spectator in (7).

Each outside crossing changes the remaining original power by
\(n\mapsto n+1\). Collecting it at that outside vertex uses the
original twist-sliding isotopy, carrying the rotations and the
orders of any intervening branches. The immediate carrier changes from \(\eta\) to
\(\eta+1\), with its disk-filling coefficient \(p\) unchanged.
If the carrier is normalized to \(\eta'=1-\eta\), with
\(\eta\in\{0,1\}\), the exact bookkeeping is
\[
 p'=p-\eta,\qquad
 \lambda\longmapsto\lambda',\qquad
 \mu\longmapsto\mu'-\eta\lambda'.
 \tag{14}
\]
This is the disk-cut transfer of a full twist in Section 5 of the
marked degree-two note. It sends the original primitive filling curve
to \(\mu'+(p-\eta)\lambda'\). Normalizing the carrier without this
basis change would lose the original marking.

## 3. The exact original source

Let \(M\) multiply by the original crossing in the full Newton
algebra \(\mathcal A_N\), let \(J\) reverse its coefficients, and put
\[
             \kappa_N=\exp\frac{\pi i(N-1)^2}{2N}.
 \tag{15}
\]
Repeated spectral roots retain their first normal derivatives.
The identities \(J^2=1\) and
\(JMJ=\kappa_NM^{-1}JM^{-1}\) imply the modular representation
generated by \(J,\kappa_N^{-1/3}M\), with the displayed logarithm.

The sums of the original and complementary magnitudes are
\(2m+k\) and \(m+2k+1\). Comparing crossing exponents in (9) gives
\[
 JM^{-b_1}J\cdots JM^{-b_m}J
 =\kappa_N^{-(m+k+1)}
       M\bigl(JM^{c_1}J\cdots JM^{c_\ell}J\bigr)M.
 \tag{16}
\]
Indeed the exponent difference is
\(-(2m+k)-2-(m+2k+1)=-3(m+k+1)\).

Let \(\mathcal P_{\mathbf b,-,N}\) and
\(\mathcal P_{\mathbf c,+,N}\) denote the full two-boundary sources.
Their coefficient matrices are respectively
\(JM^{-b_1}\cdots JM^{-b_m}\) and \(JM^{c_1}\cdots JM^{c_\ell}\).
Multiply (16) by \(J\) and use \(JMJ=M^T\). The tensor identity is
\[
 \boxed{\displaystyle
 \mathcal P_{\mathbf b,-,N}
   =\kappa_N^{-(m+k+1)}
           (R\otimes R)\mathcal P_{\mathbf c,+,N}.}
 \tag{17}
\]
This is an equality in \(\mathcal A_N\otimes\mathcal A_N\).
Both variables are canonically reduced; it is not an equality
of unreduced products at arbitrary complex arguments.

For the pendant coefficient columns,
\[
 \boxed{\displaystyle
 F_{\mathbf b,-,N}
       =\kappa_N^{-(m+k)}R F_{\mathbf c,+,N}.}
 \tag{18}
\]
Apply (16) to \(Je_0\), and use
\(JMJ e_0=M^{\mathsf T}e_0=\kappa_Ne_0\).
Thus \(MJ e_0=\kappa_NJe_0\), and the right side of (16)
becomes \(\kappa_N^{-(m+k)}M F_{\mathbf c,+,N}\).
The additional cap factor is exactly \(\kappa_N\), as also follows
from the stabilizer (13).

These equalities retain all normal data and their exact unit scalars.
The physical rotation in (11) has the separate marked justification;
the tensor formula is not an assertion of rotation invariance for
an arbitrary attached tangle.

## 4. The positive geometric presentation

**Theorem 3.** Let a selected path in an original circle tree have
the powers (1), at least one complete outside end, and all other
auxiliary circles complete. Its partially filled exterior has the
positive circle-tree decomposition associated with (7), or (12)
for a pendant path. Its outside primitive curves are carried by (14),
and its original main-component condition is unchanged.

**Proof.** Every new magnitude is at least three, except the single
vertex \((2)\). The
[negative-corridor geometry theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_negative_corridor_variational_bounds.md),
Theorem 15, also gives positive powers: replace a negative solution
\(t_v\) by \(-\overline{t_v}\). Its returns become
\(-\overline{r_{v,e}}\), its full unit charges have the positive sign,
its core imaginary parts remain negative, and the inequality
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\) is unchanged.
The isolated-vertex theorem supplies the exceptional single
positive power two.

Retain the outside crossings in their carriers and disk frames.
Their periods vanish when the outside angles are zero. The original
annular attachments, with the proper rotations transported, are
therefore the marked attachments of the new circle-tree presentation.
The [pointwise marked-completion theorem](research_positive_point_marked_completion.md)
gives its smooth hyperbolic filling. The tangle isotopy identifies
this with the original partially filled exterior. It preserves
the main strands and every outside component, so the same original
knot or link condition applies. \(\square\)

The absolute volume is the positive stationary action of the new
whole presentation:
\[
 2\pi\Re\left\{
  \sum_{\text{new edges }e}\psi(t_{e^-},t_{e^+})
  +\frac{i}{4\pi}\sum_{\text{new selected }v}c_vt_v^2
  -i\sum_{\text{new selected }v}t_v
               \right\}.
 \tag{19}
\]
Every new edge is included, including complete outside edges.
This uses the marked-completion theorem's absolute normalization.

Equations (17)--(18) supply an exact finite source with this positive
geometric presentation. They do not identify an old stationary
cycle with a new one. No equality between individual old and new
stationary actions is inferred from a finite operator identity.
A full asymptotic for arbitrary adjacent powers at least three,
or a proof of the required cycle transport, is still needed for
a volume-conjecture conclusion in that generality. Section 6 gives
the consequence when the complementary powers satisfy an already
proved asymptotic theorem.

For counting, the path (1) is fixed. Remaining powers undergo fixed
integer translations, with permutations and rotations retained.
This map is injective: no free powers are merged. Several disjoint
fixed paths add their fixed shifts at a shared outside vertex.
Thus the replacement has no infinite-fiber loss. It supplies a
geometric family containing mixed short powers, not cofinite
coverage of all assignments.

## 5. Reproducing the finite identities

Run the [checker](../experiments/check_binary_negative_corridor_reexpression.py)
with

    python3 experiments/check_binary_negative_corridor_reexpression.py \
      --output repro/results/research-binary-negative-corridor-reexpression.json

The default run checks all 2,048 binary words through length twelve
whose end entries are two. Rational arithmetic checks the complementary
fractions, full affine maps, retained rotations, pendant stabilizers,
and scalar exponents. All four proper-rotation possibilities occur.
Seven displayed words are also tested in the original full Newton
matrices at levels two through eight, giving 49 two-boundary matrix
comparisons and 49 pendant-column comparisons at 100 decimal digits.
Those matrix comparisons are diagnostics; the modular-group argument
proves (16)--(18) at every level.

The [saved output](../repro/results/research-binary-negative-corridor-reexpression.json)
records the exact examples, every matrix residual, and the SHA256
hashes of the checker and its dependencies. An independent run can
write to a different output path.

## 6. Pendant boundary asymptotics and a long closing twist

Read the coefficients in (1) and (2) from the outside boundary
towards the terminal cap. Thus the positive pendant word is
\[
 F_{\mathbf c,+}
   =T\bigl(R^{c_1}T(R^{c_2}\cdots T(R^{c_\ell})\cdots)\bigr).
 \tag{20}
\]
Its terminal power is \(c_\ell\). The other coefficients are the
successive turns to which the long-power theorem applies.

Let \(B_*\) be the integer threshold in Section 6 of
[the fixed-domain long-power theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_fixed_domain_long_power_turns.md).
Enlarge it to at least three if necessary. Let \(B_{\rm cl}\) be
the closing threshold in Section 7 of that same note; its equation
(36) gives sufficient inequalities in the common analytic constants.
Both thresholds are independent of the length of the fixed word.
Use the initial common disk inside the marked geometric charts, as
in that theorem, and include its stated final geometric enlargement
in these thresholds. This is a single choice before any word is
selected.

**Theorem 4.** Suppose
\[
       c_j\ge B_*\quad(1\le j<\ell),\qquad c_\ell\ge2.
 \tag{21}
\]
Then the canonical original pendant source for the negative binary
word has a nonzero full boundary asymptotic on a fixed complex disk,
and a Gaussian angular bound on a fixed strip. More precisely, write
the positive word's proved expansion as
\[
 F_{\mathbf c,+,N}(u)
    =\varepsilon_{\mathbf c,N}A_{\mathbf c}(u)
       e^{N W_{\mathbf c}(u)}(1+O_{\mathbf c}(N^{-1})).
 \tag{22}
\]
Here \(u\) is the original remaining boundary angle, the phase is
even and holomorphic, and the holomorphic amplitude has no zero on
the chosen closed disk. Then
\[
 \boxed{\displaystyle
 F_{\mathbf b,-,N}(u)
  =\kappa_N^{-(m+k)} C_{N,1}\varepsilon_{\mathbf c,N}
    A_{\mathbf c}(u)
    \exp N\left\{W_{\mathbf c}(u)+\frac{i u^2}{4\pi}\right\}
    (1+O_{\mathbf b}(N^{-1})),\qquad
 C_{N,1}=\exp\!\left(\frac{\pi i(N-1)^2}{4N}\right).}
 \tag{23}
\]
The disk and strip can be chosen independently of the word length
and coefficients satisfying (21). Polynomial prefactors, amplitude
sizes, error constants and the starting level may depend on the
entire fixed word. Both level parities and all original first normal
derivatives are included.

**Proof.** Start with the terminal power \(c_\ell\), then apply the
fixed-domain theorem to \(c_{\ell-1},\ldots,c_1\), in that order.
Its Section 6 gives (22), a common phase bound and positive curvature,
and a common bound
\[
 |F_{\mathbf c,+,N}(x+iy)|
 \le C_{\mathbf c}N^{d_{\mathbf c}}
 \exp N\{\Re W_{\mathbf c}(0)
               -\gamma(1-\cos x)+C y^2\},
 \qquad |x|\le\pi,\quad |y|\le h,
 \tag{24}
\]
with \(\gamma,h>0\). In (18), multiplication by \(R\) is multiplication
in the full original Hermite quotient, followed by its canonical
representative; it is not multiplication by an arbitrary analytic
interpolant. Apply Theorem 1 of
[boundary crossing preservation](research_boundary_crossing_packet_preservation.md)
with the fixed power \(+1\). That theorem gives (23) and preserves
a bound of the form (24) on a possibly smaller common disk and
strip. Its family statement gives the asserted uniformity. The exact
scalar in (18) has modulus one and introduces no further error.
\(\square\)

The run-length conditions in this theorem are explicit. If \(k=0\),
there is a single complementary terminal power \(m+1\); (21) imposes
no lower bound on the length \(m\ge1\). If \(k\ge1\), (21) says
\[
 \begin{split}
 r_0&\ge\max(1,B_*-2),\\
 r_j&\ge\max(0,B_*-3)\qquad(1\le j<k),\\
 r_k&\ge1 .
 \end{split}
 \tag{25}
\]
In particular the final run, adjacent to the cap, need not be long.
There may be arbitrarily many threes, provided each preceding run
has the indicated length. All lengths and powers are fixed before
the level \(N\) tends to infinity.

**Corollary 5.** Assume (21). Give the remaining original circle a
fixed signed closing power \(a\), and suppose
\[
                         |a+1|\ge B_{\rm cl}.
 \tag{26}
\]
Under the original knot and framing conditions, the cylindrical
closure of this negative pendant word satisfies the volume
conjecture. Its complete source has a nonzero asymptotic
\[
 \begin{split}
 Z_{\mathbf b,a,N}
   &=\phi_N(R^a F_{\mathbf b,-,N})\\
   &=\kappa_N^{-(m+k)}
        \phi_N(R^{a+1}F_{\mathbf c,+,N})\\
   &=\kappa_N^{-(m+k)}\varepsilon_{\mathbf c,N}C_{N,a+1}
       N^{3/2}D_{\mathbf c,a+1}
       e^{N\mathcal V_{\mathbf c,a+1}}
       (1+O_{\mathbf b,a}(N^{-1})),
       \qquad D_{\mathbf c,a+1}\ne0 .
 \end{split}
 \tag{27}
\]
The invariant is the original zero-framed knot invariant, up to the
unit normalization already retained in the original source convention.
Consequently
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
       =2\pi\Re\mathcal V_{\mathbf c,a+1}
       =\operatorname{Vol}(S^3\setminus K).
 \tag{28}
\]

**Proof.** The middle line of (27) is the exact quotient identity
(18), contracted with the original trace. Section 7 of the
fixed-domain theorem applies with the closing power \(c_0=a+1\).
It proves the last line of (27), including its nonzero coefficient,
both parities and every trace normal. Its phase is
\[
 \mathcal V_{\mathbf c,a+1}
   =W_{\mathbf c}(s_*)+
       \frac{i(a+1)s_*^2}{4\pi}-is_*,
 \qquad
 W_{\mathbf c}'(s_*)+
       \frac{i(a+1)s_*}{2\pi}-i=0,
 \tag{29}
\]
on its selected small branch. The pendant isotopy (12), followed by
the original closure, gives the same marked knot as this positive
word with closing power \(a+1\). The peripheral shear is exactly
(14); neither the original meridian nor the disk longitude is
silently reset. The marked geometric part of the closing theorem
identifies \(2\pi\Re\mathcal V_{\mathbf c,a+1}\) with the absolute
volume of this knot complement. All displayed scalar factors have
modulus one, so (28) follows. \(\square\)

The original component test is essential: the closure must have one
main component and satisfy the original exclusion of internal closed
components. It is transported by the literal tangle isotopy. A
sufficient condition for (26) is \(|a|\ge B_{\rm cl}+1\); (26) is the
precise translated condition. For each fixed negative binary word
satisfying (21), the map of remaining assignments is the injection
\(a\mapsto a+1\).
Thus the conclusion includes all sufficiently long signed closing
assignments on that stratum, with no identification of distinct free
parameters.

For a path with two free outside boundaries, (17) is still an exact
identity with both variables and all normal data. The one-boundary
theorem used above does not by itself give a joint two-boundary
asymptotic. Such a replacement can be made inside a whole marked tree
and the existing tree theorem applied if the *transformed whole tree*
satisfies its hypotheses, with all outside shifts and rotations
retained. No standalone joint packet for an arbitrary complementary
chain is asserted here.

## 7. What repeated complementation can reach

The complementary fraction is defined for every finite list
\(\mathbf b=(b_1,\ldots,b_m)\) with \(b_j\ge2\). Let \(D(\mathbf b)\)
be the unique list with entries at least two and
\[
 [D(\mathbf b)]_-=\frac{[\mathbf b]_-}{[\mathbf b]_--1}.
 \tag{30}
\]
The ceiling algorithm in the
[definite rational normal form](research_definite_rational_corridor_normal_form.md),
Section 2, proves uniqueness. Since \(x\mapsto x/(x-1)\) is an
involution, so is \(D\).

**Proposition 6.** The list \(D(\mathbf b)\) has every entry at
least three if and only if \(\mathbf b\) is a binary list with both
end entries two, other than the singleton \((2)\).
With the original outside frames, the only uniform-sign chain
forms with magnitudes at least two, allowing integral twists at
the two ends and the retained proper rotations, are the negative
form \(\mathbf b\) and the positive form \(D(\mathbf b)\).
The same assertion holds for a pendant word with its original
outside frame and cap.

**Proof.** For a one-entry list \((a)\),
\[
               D((a))=(2^{a-1}).
 \tag{31}
\]
If the complementary list for a tail is
\((d_1,d_2,\ldots)\), prepending \(a\ge2\) to the original
list changes it to
\[
        (2^{a-2},d_1+1,d_2,\ldots).
 \tag{32}
\]
Here an empty string is omitted. Equation (32) follows from (4):
prepending two increments the first entry, and each further unit
in \(a\) inserts a two at the front.

In this recursion, only the first entry of an existing list can
ever increase. If the final entry \(b_m\) is at least three,
(31) initially has a two that can never be increased. If any
other \(b_j\ge4\), (32) inserts at least two leading twos;
the second of them can never be increased. If \(b_1\ge3\),
the final application of (32) leaves a leading two. Thus absence
of twos in the complement requires entries in \(\{2,3\}\) and
both ends two. Formula (2) proves sufficiency, except that the
singleton two has itself as complement.

For the statement with two boundaries, write the normalized
matrix of the original negative word as
\[
             \begin{pmatrix}A&B\\C&D\end{pmatrix},
             \qquad 0<A,D<C,\qquad C/A=[\mathbf b]_- .
 \tag{33}
\]
Integral end twists do not change \(A,D\) modulo \(C\), and the
proper rotations have identity linear part on the pillowcase.
A uniform-negative chain with entries at least two already has
its diagonals in this normalized range, so uniqueness of the
ceiling expansion forces its list to be \(\mathbf b\). For a
uniform-positive chain the normalized diagonal residues are
the complementary ones \(C-A,C-D\). Its list is therefore
uniquely \(D(\mathbf b)\), with the two end twists \(+1\).
The full affine comparison retains the appropriate rotation
as in (10)--(11).

For a pendant word, its normalized slope is
\(x=1/[\mathbf b]_-\in(0,1)\). A negative chain preceded by an
integer twist has slope \(r+1/[\mathbf d]_-\); equality to \(x\)
forces \(r=0\) and \(\mathbf d=\mathbf b\).
A positive chain has slope \(r-1/[\mathbf d]_-\); equality
forces \(r=1\) and \(\mathbf d=D(\mathbf b)\).
The established cap stabilizer supplies the literal isotopy and
does not enlarge either list. \(\square\)

Consequently the all-magnitudes-at-least-three geometric theorem,
combined only with repeated marked complementation and end twists,
covers exactly two types of negative lists: those already having
all entries at least three, and the binary lists of Proposition 6.
The separately proved isolated power two is an additional elementary
case. For example,
\[
                         (3,2,3)\longleftrightarrow(2,4,2)
 \tag{34}
\]
has a two in both normalized forms. This is an obstruction to
that particular reduction strategy, not to a positive subdivision
of the actual filled manifold. Local replacements may produce a
mixed-sign chain, but if their eventual result is a uniform-sign
chain in the same outside frames, the same uniqueness argument
still applies.

No conclusion here permits a quarter-turn of an outside attachment
while leaving its primitive curves untouched. Such a move changes
the retained boundary frame and would require a separate geometric
attachment argument. The fixed integer end shifts and proper
rotations already allowed preserve the injective assignment
bookkeeping of Section 2.

