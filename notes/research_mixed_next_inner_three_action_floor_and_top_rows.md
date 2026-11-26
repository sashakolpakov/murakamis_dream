# A stronger inner action floor and a removable top strip of second-edge rows

Private source proof, 8 November 2026. The original continued
inner action has a uniform written lower bound strictly above
\(3/2\). Together with the complete terminal insertion theorem,
this pays a fixed strip of retained second-edge indices near
\(N/2\), inside the full inner Hermite trace. The conclusion
holds whether the first edge is full or shortened.

No mathematical numerical evaluation, saved-value calculation,
or frozen-source edit is used. No pointwise kernel deletion
or complete inner asymptotic is asserted.

## 1. Original family and action

Let
\[
 \begin{gathered}
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},\\
 t_*(u)=a_*(u)-iH(u),\qquad
 0<a_*<\pi/2,\quad1/2<H<1,\\
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u).
 \end{gathered}                                                     \tag{1}
\]
The branch, charge, and additive constant are the unchanged
ones in [the original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md).
Only already proved phase comparisons will be used to bound
this target action.

**Proposition 1.** Uniformly on \(\mathcal U_+\),
\[
 \boxed{\qquad s(u)>\frac32+\frac{853}{63000}.\qquad}
                                                                    \tag{2}
\]

*Proof.* Put \(t_R=\pi/2-iH(u)\). Original horizontal
concavity, as used in
[the complete inner boundary proof, Section 2](research_mixed_next_inner_three_far_samples_and_verticals.md),
gives
\[
 s(u)\ge\Re\psi(t_R,0)+\Re\psi(t_R,b-iK)-\frac H4.
                                                                    \tag{3}
\]
That proof retains the original principal returns and shows
\[
 \Re\psi(t_R,b-iK)\ge
       \psi(\pi/2,\pi/2)-\frac{HK}{2\pi}
       >\frac{50}{63}-\frac{HK}{2\pi}.
                                                                    \tag{4}
\]
In detail, its equations (12)--(16) first move the real
outside angle to \(\pi/2\) and then bound the downward
height cost by \(HK/(2\pi)\). Its equations (17)--(18)
use the increasing first height and the same real-corner
constant. Thus (4) is valid for the full closed actual
family, not only for a real outer angle.

The complete-end leg has a sharper separate bound.
[Complete-edge gap, equations (12)--(14)](research_internal_pair_complete_edge_gap.md)
gives, for \(0\le H\le1\),
\[
 \Re\psi(\pi/2-iH,0)
  >\frac{239}{250}
    +\frac{H^2/2-H^4/24}{\sqrt2\,\pi}.
                                                                    \tag{5}
\]
This is the original complete constant plus the integrated
original return; no action normalization is changed.
The elementary inequalities
\[
 H^2/2-H^4/24\ge\frac{11H^2}{24},\qquad
 \sqrt2<\frac32,\qquad \pi<\frac{22}{7}
                                                                    \tag{6}
\]
imply that the correction in (5) is at least \(7H^2/72\).
The strict constant in (5) persists also at \(H=0\).
Moreover \(K\le1/2\) and \(\pi>3\) give
\[
                     \frac{HK}{2\pi}+\frac H4\le\frac H3 .
                                                                    \tag{7}
\]
Combining (3)--(7),
\[
 s(u)>
       \frac{239}{250}+\frac{50}{63}
                         +\frac{7H^2}{72}-\frac H3.
                                                                    \tag{8}
\]
The last two terms decrease on \([0,1]\), since
\(7H/36-1/3<0\). Their value at \(H=1\) is
\(-17/72\). The exact constant is
\[
 \frac{239}{250}+\frac{50}{63}-\frac{17}{72}
                  =\frac32+\frac{853}{63000},
                                                                    \tag{9}
\]
which proves (2). \(\square\)

## 2. A zero-safe half-index norm on the actual terminal strip

Use the original Newton polynomials, with
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,\qquad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),
                                                                    \tag{10}
\]
and the original \(c_a=2\cos((2a+1)\pi/N)\) and sine
factorials. For \(z=\theta+ih\), keep the real product
potential
\[
 V_z(y)=\int_0^y
       \log|2\cos(2\pi s)+2\cos z|\,ds-2J(y),\qquad
 J(y)=\int_0^y\log(2\sin\pi s)\,ds .
                                                                    \tag{11}
\]
The original finite midpoint estimate, including its
numerator zeros, gives
\[
 |e_j(-2\cos z)|\le C N^A e^{N V_z(j/N)}
              \quad(|\theta|\le\pi,\ |h|\le2/3,\ 0\le j\le D).
                                                                    \tag{12}
\]
This is the same estimate and strip already proved in
[the outer boundary source, Section 2](research_mixed_next_outer_far_angles_and_verticals.md).
The exact circle-log identity gives
\[
                         V_z(1/2)=|h|/2.
                                                                    \tag{13}
\]
It is also proved directly, with the half-grid endpoint
error, in
[the far-negative source, equations (11)--(13)](research_mixed_next_inner_three_far_negative_source.md).

The potential (11) is jointly continuous in \(y,\theta,h\)
on a neighborhood of
\(\{1/2\}\times[-\pi,\pi]\times[-2/3,2/3]\).
For clarity, factor its numerator into the two shifted
cosines. Away from a zero their logarithms are continuous
with bounded derivatives on compact subsets. On an interval
of length \(\delta\) containing a possible zero, their
integrals have a uniform absolute bound
\(C\delta(1+|\log\delta|)\); moving a zero off the real
axis only regularizes the same estimate. The denominator
is regular near \(y=1/2\). These estimates prove the
claimed uniform continuity, including coalescing or
endpoint zeros.

Set the fixed tolerance
\[
                              \varepsilon=\frac1{300}.
                                                                    \tag{14}
\]
Choose one fixed \(0<\delta<1/10\) so small that
\[
 V_z(y)\le |h|/2+\varepsilon
 \quad\left(\frac12-\delta\le y\le\frac12,\quad
                |\theta|\le\pi,\ |h|\le\frac23\right).
                                                                    \tag{15}
\]
Existence follows from (13) and the just-proved uniform
continuity. The choice is independent of \(N\).
No numerical value of \(\delta\) is needed or evaluated.

Define the exact integer threshold
\[
                    J_N=\left\lceil N(1/2-\delta)\right\rceil .
                                                                    \tag{16}
\]
For every sufficiently large \(N\) and every
\(J_N\le j\le U\), equations (12)--(15) give
\[
 \begin{split}
 \|e_j\|_{2/3}
  &:=\sup_{\substack{|\theta|\le\pi\\|h|\le2/3}}
                      |e_j(-2\cos(\theta+ih))|
       \le C N^A e^{N(1/3+\varepsilon)},\\
 |e_j(-2\cos u)|
       &\le C N^A e^{N(K/2+\varepsilon)}
        \le C N^A e^{N(1/4+\varepsilon)}
                           \qquad(u\in\mathcal U_+).
 \end{split}                                                       \tag{17}
\]
The retained endpoints satisfy \(U/N<1/2\) at both
parities. Every actual row in (16)--(17) is covered;
no replacement of a zero by a relative expansion occurs.

## 3. The complete terminal insertion pays these rows

Let \(R_N,\phi_N\) be the original crossing and full
Hermite closing functional, and put \(z_u=-2\cos u\).
The original complete terminal insertion estimate is
\[
 |\phi_N[R_N^3 K_N^{\rm ord}(-2,\cdot)\,I]|
       \le C_\tau N^{A_\tau}
          e^{N(M_{\rm term}+\tau)}\|I\|_{2/3},
                         \qquad \deg I\le N ,
                                                                    \tag{18}
\]
where \(M_{\rm term}<17/20\). The source is
[the complete paired-right insertion theorem, Section 4](research_mixed_next_right_paired_terminal_insertion.md),
with the eligible smaller-strip extension in
[insertion recoupling, Section 4](research_mixed_next_right_insertion_recoupling_and_norm.md)
and [the outer boundary proof, equation (24)](research_mixed_next_outer_far_angles_and_verticals.md).

The norm height \(2/3\) has a fixed margin above every
original terminal trace contour. Indeed their maximum
height \(h_{\rm tr}\) satisfies
\[
 \cosh h_{\rm tr}=(1+\sqrt2)/2
             <11/9<\cosh(2/3).
                                                                    \tag{19}
\]
Thus the insertion's required fixed angular derivatives
cost only constants in this margin; the physical first
normals cost only polynomial factors by Markov at the
original degree bound. Equation (18) retains the removed
wire and angular rows, the odd simple node, both aliases,
all wire sides and angular connectors, every nested end
surface, and the full rational trace kernel. It is a
bound for that complete source, not a phase-only estimate
or an evaluation functional substituted for the trace.

Apply (18) to the literal insertion \(I=e_j\), which has
degree \(j\le U<N\), with \(\tau=\varepsilon\). Multiply
by its actual outside coefficient from (17). For any
subset \(\mathcal J\subset\{J_N,\ldots,U\}\),
\[
 \begin{split}
 &\sum_{j\in\mathcal J}
 |e_j(z_u)\,
        \phi_N[R_N^3 K_N^{\rm ord}(-2,\cdot)e_j]|\\
 &\qquad\le C N^A
       e^{N\{M_{\rm term}+1/3+1/4+3\varepsilon\}}
       \le C N^A e^{433N/300}.
 \end{split}                                                       \tag{20}
\]
Here
\[
               \frac{17}{20}+\frac13+\frac14=\frac{43}{30},
              \qquad 3\varepsilon=\frac1{100}.
                                                                    \tag{21}
\]
The finite number of rows is absorbed in \(N^A\).
Since
\[
                \frac32-\frac{433}{300}-\frac1{20}
                                     =\frac1{150}>0,
                                                                    \tag{22}
\]
Proposition 1 and polynomial absorption prove
\[
 \boxed{\quad
 \sum_{j\in\mathcal J}
 |e_j(z_u)\,
        \phi_N[R_N^3 K_N^{\rm ord}(-2,\cdot)e_j]|
                 \le C e^{N(s(u)-1/20)} .
 \quad}                                                           \tag{23}
\]
This is an absolute bound on the individual traced rows,
uniform over all such subsets and both level parities.

## 4. The first shortening and its subset errors

It is necessary to justify separately the replacement
of the full first edge in (23). Write
\[
 \mathcal H_N(x)
   =K_N^{\rm ord}(-2,x)-K_N^{<,\rm ord}(-2,x).
                                                                    \tag{24}
\]
The exact even and odd physical-value contractions of
[the first-edge tail theorem, equations (8) and (16)](research_mixed_next_inner_three_first_edge_tail_contraction.md)
apply to every spectator polynomial, hence to \(e_j\)
for each retained \(j\). Their coefficients have modulus
at most two; at even levels the complete-end tail
coefficients have size at most \(\sqrt{N-1}\); at odd
levels the simple endpoint has coefficient
\(C_{N,3}\) of modulus one and is retained.

For every subset \(\mathcal J\subset\{0,\ldots,U\}\),
the original real and complex Newton bounds therefore give
\[
 \sum_{j\in\mathcal J}
 |e_j(z_u)\phi_N[R_N^3\mathcal H_N e_j]|
          \le C N^A e^{N(b_2+2/3)} .
                                                                    \tag{25}
\]
This is the same complete physical estimate as in that
source, now applied before the triangle inequality over
the chosen rows. Explicitly each surviving term contains
one real value \(e_j(c_a)\), of rate at most \(b_2\),
and one actual outside value \(e_j(z_u)\), of rate at
most \(2/3\). Their finite counts and every other factor
are polynomially bounded. The odd simple-node value uses
the same real Newton bound at \(c_m=-2\); it is not assumed
to have polynomial size. This proves (25) for arbitrary
subsets without extracting a bound from a coherent sum.

The stronger action floor improves the old deletion gap.
Indeed
\[
 b_2+\frac23
       <\frac{729}{1250}+\frac23
        =\frac{4687}{3750}
        =\frac54-\frac1{7500}.
                                                                    \tag{26}
\]
Equations (2),(25)--(26), with polynomial absorption,
give the absolute subset estimate
\[
 \boxed{\quad
 \sum_{j\in\mathcal J}
 |e_j(z_u)\phi_N[R_N^3\mathcal H_Ne_j]|
                   \le C e^{N(s(u)-1/4)} .
 \quad}                                                           \tag{27}
\]
In particular the whole first-edge deletion has gap
\(1/4\) on this actual family.

Subtract (27) from the literal row expression in (23)
and use the triangle inequality. The complete top-strip
bound for a shortened first edge follows:
\[
 \boxed{\quad
 \sum_{j\in\mathcal J}
 |e_j(z_u)\,
   \phi_N[R_N^3K_N^{<,\rm ord}(-2,\cdot)e_j]|
                    \le C e^{N(s(u)-1/20)},
 \quad\mathcal J\subset\{J_N,\ldots,U\}.
 \quad}                                                           \tag{28}
\]
The original first normals and all crossing scalars were
retained in both terms of this subtraction.

## 5. Exact remaining finite source

Define the more strongly truncated second kernel by
\[
 K_N^\delta(x,z)=\sum_{j=0}^{J_N-1}e_j(x)e_j(z),
 \qquad J_N=\lceil N(1/2-\delta)\rceil.
                                                                    \tag{29}
\]
For sufficiently large \(N\), \(J_N\le U\). Let \(Q_N(u)\)
be the original inner source with full first edge and
second edge shortened at \(U\), as in
[the exact low-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md).
The complete trace identities and (23),(27)--(28) prove
\[
 \boxed{\quad
 Q_N(u)=
 \phi_N^{(x)}
   [R_N(x)^3K_N^{<,\rm ord}(-2,x)K_N^\delta(x,z_u)]
                   +O(e^{N(s(u)-1/20)}).
 \quad}                                                           \tag{30}
\]
The error bound is uniform on \(\mathcal U_+\), at both
parities, with the original full Hermite trace and no
additional scalar.

The surviving source in (30) has first indices \(0\le k\le U\)
and second indices \(0\le j<J_N\). No retained physical
row has been evaluated away from its original finite
definition. The conclusion concerns their traced sum;
it is not pointwise equality on an angular contour,
does not by itself transfer the previous partial-current
asymptotic to the new integrand, and does not estimate a
subsequent unbounded outer functional.
