# The closed right paired contour as a terminal-three insertion

Private research deduction, 8 November 2026. The complete old-filter
right-half rectangle reduces exactly to one original terminal-three
Hermite trace with a coherent polynomial insertion of degree less than
\(N/2\), plus an already paid first-coordinate deletion. The full
terminal-source proof gives an upper bound in the strip norm of this
insertion. No estimate of that norm at the required next action is
asserted here.

The vertical sides and the possible half-grid strip are explicit.
Thus the closed rectangle is not identified with the remaining open
horizontal integrals. All identities retain both Fourier sectors,
the original polynomial forcing, and both level parities. No numerical
evaluation or change to a frozen source is used.

## 1. Exact complementary rows of the paired finite source

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
 P_j=(r;r)_j,\quad p_j(Y)=(rY;r)_j,\quad f_j(Y)=p_j(Y)/P_j.
 \tag{1}
\]
The letter \(q\) in this note is the quantum parameter; real contour
coordinates are written explicitly. For \(\beta=0,1\), retain
\[
 C_{\beta,N}(Y,Z)=\sum_{j=0}^{D}
       \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},\qquad
 \psi_{\beta,j}(Z)=\frac{p_j(Z)}{P_j^{1+\beta}}.
 \tag{2}
\]
Let \(E_N=F_N^{\rm mid}\) be the unchanged old filter of the
[paired meromorphic rectangle, Section 1](research_mixed_next_paired_meromorphic_rectangle.md):
\[
 \begin{gathered}
 E_N=(I-\Pi_{\rm end})(F_{34,N}-R_N^a),\quad
 A_N=\lceil23N/24\rceil,\quad l_N=\lfloor\delta N\rfloor,
 \quad B_N=\lceil11N/12\rceil,\quad 0<\delta<1/40,\\
 E_N(w,r^b)=0\quad(b\le l_N\text{ or }b\ge B_N),\qquad
 d_N(r^b)=P_b^{-1},\quad \deg d_N\le D.
 \end{gathered}
 \tag{3}
\]
In particular \(d_N\) is the full forced interpolation polynomial.
The exact paired kernel is
\[
 K_N(y)=\frac{N E_N(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}{1-Y^N},
 \qquad Y=e^{-2\pi iy}.
 \tag{4}
\]
We work at this conditional-message normalization, before the original
outgoing ordinary-boundary observation. That observation and its
scalar from the [next-attachment identity](research_mixed_three_four_next_conditional_attachment.md)
are unchanged. In particular (4) already contains its contour
extraction factor \(+N\).

Write \(\tau_k=(-1)^k r^{k(k+1)/2}=P_k/\overline{P_k}\).
The complementary product identities in
[the exact reflection theorem, Section 2](research_mixed_next_lower_complement_exact_reflection.md)
give
\[
 P_{D-k}=\frac N{\overline{P_k}},\qquad
 p_{D-k}(Y)=\frac{p_D(Y)\tau_kY^{-k}}{p_k(Y^{-1})},\qquad
 p_D(Y)=\frac{1-Y^N}{1-Y}.
 \tag{5}
\]
The apparent poles in (5) cancel polynomially. Substituting
\(j=D-k\) in (2), with both numerator factors retained, yields
\[
 C_{\beta,N}(Y,Z)=
 \frac{Y^{-D}p_D(Y)p_D(Z)}{N^{2+\beta}}
 \sum_{k=0}^{D}
   \frac{Z^{-k}\overline{P_k}^{\,\beta}}
           {f_k(Y^{-1})f_k(Z^{-1})}.
 \tag{6}
\]
Indeed \(\tau_k^2\overline{P_k}^{\,2+\beta}
=P_k^2\overline{P_k}^{\,\beta}\); no row chirp is omitted.
Canceling the outgoing apparent poles before using (4) gives the
particularly useful meromorphic identity
\[
 \boxed{\quad
 K_N(y)=E_N(w,Y)d_N(Y)Y^{-D}
   \sum_{k=0}^{D}
       \frac{\psi_{\beta,D-k}(Z)}{(1-Y)f_k(Y^{-1})}.
 \quad}
 \tag{7}
\]
The outgoing coefficients in (7) are polynomials, so (7) is valid
also at every outgoing numerator zero. It does not replace
\(d_N\) by a homogeneous recurrence solution.

For every \(0\le k<N\), the exact partial fractions are
\[
 \boxed{\quad
 \frac1{(1-Y)f_k(Y^{-1})}
  =\sum_{b=0}^{k}
       \frac{P_k}{\overline{P_b}P_{k-b}}\frac1{r^b-Y}.
 \quad}
 \tag{8}
\]
To verify them, write the left side as
\(P_kY^k/[(1-Y)\prod_{h=1}^k(Y-r^h)]\).
It is proper rational. Its residue at one is \(-1\).
At \(Y=r^b\), \(1\le b\le k\), its residue is
\(-P_k/(\overline{P_b}P_{k-b})\), using
\((1-r^b)\overline{P_{b-1}}=-r^b\overline{P_b}\).
These are all its poles, proving (8).

Thus each complementary row has physical poles only at indices
\(0\le b\le k\). Every deleted-node pole is removed termwise
by (3). No bound on reciprocal factors through their zeros is
being assumed.

## 2. The exact right rectangle, including every boundary term

Keep the actual base heights
\[
             -.102<h_*<-.001,\qquad H=1/100,
 \tag{9}
\]
and define
\[
 M_N=\lceil N/2\rceil,\qquad
 L_N=\frac{M_N-1/2}{N},\qquad
 \mathscr C_N=[L_N,1]+i[h_*,H].
 \tag{10}
\]
The left side is on a half grid. The node at the right seam is
removable by (3). With counterclockwise orientation, the exact
residue formula of the paired rectangle proves
\[
 \mathscr R_N^{\rm cl}:=\int_{\partial\mathscr C_N}K_N(y)\,dy
   =\sum_{b=M_N}^{B_N-1}
            \frac{E_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
 \tag{11}
\]
There is no additional \(N\) outside this integral: the original
factor in (4) is already included. The formula holds whenever the
displayed ranges are nonempty, with empty-sum conventions otherwise.

By (8), the terms \(k<M_N\) have no poles inside this rectangle.
Their entire closed-boundary integrals vanish exactly. This does
not remove them from either open horizontal or either vertical
current. In particular the \(\beta=1\) factor
\(\overline{P_k}\) in (6), whose limiting rate is negative for
\(0<k/N<1/2\), belongs here to the pole-free complementary rows.
The right-node residue block only sees \(k\ge M_N\), for which
the sine-factorial rate \(J(k/N)\) is nonnegative. Factorial decay
of the former rows therefore does not by itself pay (11).

For completeness define the oriented open horizontal difference
\[
 \mathscr H_N(c)=
    \int_{[c,1]+ih_*}^{\longrightarrow}K_N(y)\,dy
     -\int_{[c,1]+iH}^{\longrightarrow}K_N(y)\,dy,
 \qquad
 V_N(c)=i\int_{h_*}^{H}K_N(c+ih)\,dh.
 \tag{12}
\]
Only \(c=L_N,1\) is used for the verticals, so their paths are
regular after the stated removals. The exact orientation is
\[
 \mathscr R_N^{\rm cl}=
       \mathscr H_N(L_N)+V_N(1)-V_N(L_N).
 \tag{13}
\]
One has \(L_N\le1/2\), with equality at odd levels. Put
\[
 J_N^{\rm grid}=
     \int_{[L_N,1/2]+ih_*}^{\longrightarrow}K_N(y)\,dy
      -\int_{[L_N,1/2]+iH}^{\longrightarrow}K_N(y)\,dy.
 \tag{14}
\]
The exact lower-right versus upper-right difference is consequently
\[
 \boxed{\quad
 \mathscr H_N(1/2)=\mathscr R_N^{\rm cl}
              -V_N(1)+V_N(L_N)-J_N^{\rm grid}.
 \quad}
 \tag{15}
\]
No estimate for the three added terms is inferred from their
length, from the deleted seam node, or from the right-node sum.
On the complete paired period the seam vertical has its opposite
partner, as in the
[cyclic horizontal reduction](research_mixed_next_paired_cyclic_horizontal_reduction.md).
That cancellation is not a deletion from (15) in isolation.

## 3. The full right-node prefix becomes one coherent insertion

Let \(\kappa=q^{D^2/2}\), and use the original ordinary Newton
basis and trace
\[
 \begin{gathered}
 S_j=|P_j|,\quad c_j=2\cos((2j+1)\pi/N),\quad
 e_j(t)=S_j^{-2}\prod_{h<j}(c_h-t),\quad v(t)=(e_0(t),\ldots,e_D(t))^T,\\
 K_N^{\rm ord}(s,t)=\sum_{j=0}^{D}e_j(s)e_j(t),\quad
 \phi_N(f)=(-1)^D N^2[t^D]\operatorname{rem}_{\mathcal Q_N} f,
 \quad \mathcal Q_N(t)=2T_N(t/2)+2,
 \end{gathered}
 \tag{16}
\]
where \(T_N\) in (16) is the standard Chebyshev polynomial.
Let \(\mathcal R_N(t)\) denote the original crossing polynomial,
whose multiplication matrix is \(M\), and set \(A_3=JM^3\).
The original exact lowered-word identity is
\[
 \frac{F_{34,N}(w,r^b)}{P_b}
       =\frac{(-q)^b}{\kappa^2N}\ell_b(w),\qquad
 \ell_b(w)=(v(w)^TA_3^2)_b.
 \tag{17}
\]
This is an identity for the full prefix and both Fourier sectors;
see [the dual observation, Section 3](research_mixed_next_lowered_word_dual_observation.md).

For \(b\ge M_N\), put \(n=D-b<\lfloor N/2\rfloor\). The
[full high-Newton radical contraction](research_high_newton_radical_contraction.md)
gives
\[
 \begin{split}
 \ell_b(w)&=\sum_{j=0}^{n}b_{nj}\mathcal R_N(c_j)^3
                           \mathcal K_{3,N}(w,c_j),\\
 b_{nj}&=(-1)^{n+j}
       \frac{2\sin((2j+1)\pi/N)S_n^2}{S_{n-j}S_{n+j+1}},
           \qquad |b_{nj}|\le2,\\
 \mathcal K_{3,N}(w,c_j)&=
       \phi_N^{(t)}[\mathcal R_N(t)^3
                 K_N^{\rm ord}(w,t)K_N^{\rm ord}(c_j,t)].
 \end{split}
 \tag{18}
\]
Every crossing value retains its original phase
\(\mathcal R_N(c_j)=\kappa(-1)^j q^{j(j+1)}\).

Define the following single coherent polynomial before estimating
any of its summands:
\[
 \mathcal I_{\beta,N}(t,Z)=
 \sum_{b=M_N}^{B_N-1}(-q)^b C_{\beta,N}(r^b,Z)
       \sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                     K_N^{\rm ord}(c_j,t).
 \tag{19}
\]
Physical termination gives
\(\deg_Z C_{\beta,N}(r^b,Z)\le D-b\), and
\(K_N^{\rm ord}(c_j,t)=\sum_{h=0}^j e_h(c_j)e_h(t)\).
Hence
\[
        \deg_t\mathcal I_{\beta,N},\ \deg_Z\mathcal I_{\beta,N}
                  \le\lfloor N/2\rfloor-1<N/2.
 \tag{20}
\]
This excludes the odd-level simple middle node exactly; no normal
has been dropped by a rounding convention.

Since at the retained nodes \(E_N=F_{34,N}-R_N^a\), equations
(11), (17)--(19) prove the exact source reduction
\[
 \boxed{\quad
 \mathscr R_N^{\rm cl}=
   \frac1{\kappa^2N}\phi_N^{(t)}
       [\mathcal R_N(t)^3K_N^{\rm ord}(w,t)
                                    \mathcal I_{\beta,N}(t,Z)]
          -\mathcal D_{\beta,N}^{a,\rm rt}(w,Z),
 \quad}
 \tag{21}
\]
where the deletion is retained explicitly as
\[
 \mathcal D_{\beta,N}^{a,\rm rt}
   =\sum_{b=M_N}^{B_N-1}
             \frac{R_N^a(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
 \tag{22}
\]
No Fourier coefficient has been estimated separately in (21).

## 4. A complete terminal-source insertion norm bound

Let \(M_{\rm term}=\Re S_3(0)\) be the original terminal-three
action from the
[complete terminal theorem](research_three_crossing_terminal_filling.md).
For a polynomial \(I\), put
\[
 \|I\|_{\rm strip}=
   \sup_{\substack{-\pi\le\Re\theta\le\pi\\
                    |\Im\theta|\le\log2}}
                         |I(-2\cos\theta)|.
 \tag{23}
\]
The complete insertion argument in
[high coefficients by terminal insertion, Section 3](research_mixed_next_high_coefficients_terminal_insertion.md)
proves the following operator bound for every polynomial of degree
at most \(N\):
\[
 \left|\phi_N[\mathcal R_N^3K_N^{\rm ord}(w,\cdot)I]\right|
 \le C_\tau N^{A_\tau}
            e^{N(M_{\rm term}+\tau)}\|I\|_{\rm strip}.
 \tag{24}
\]
The constants do not depend on the polynomial. The bound holds for
all real ordinary \(w\in[-2,2]\) and, for each prescribed
\(\tau>0\), on a sufficiently small fixed complex disk about
\(-2\). Here is the full source justification for applying that
argument to a coherent insertion instead of its individual summands.

* The original removed wire rows are bounded through the exact
  physical derivative-sampling formula, after multiplying the
  whole row polynomial by \(I\). Markov's inequality on the real
  spectral interval applies at degree at most \(2N\), giving only
  polynomial cost. The original low- and high-wire rates retain
  their strict gaps below \(M_{\rm term}\), multiplied by
  \(\|I\|_{\rm strip}\). No bound on a signed row sum is
  assigned to its summands.
* The removed angular nodes are treated with the same complete
  polynomial before physical sampling. Both the value and the
  original first normal have the old angular-end rate times
  \(\|I\|_{\rm strip}\), with polynomial cost. The odd simple
  node remains included.
* On the original retained trace contours the insertion is
  \(I(-2\cos\theta)\). It is even in \(\theta\), preserving
  the exact pairing of angular connectors, and is independent of
  the private wire coordinate. Thus it multiplies the main
  rectangle, both horizontal aliases, both complete wire-cut
  sides, both angular connectors, and all nested endpoint
  surfaces before any estimate is taken.
* Every one of those trace contours satisfies
  \(|\Im\theta|\le h_t<\log2\), with the same fixed strict
  margin as in the cited insertion proof. Cauchy's formula in
  that margin bounds the required angular derivatives by
  \(C\|I\|_{\rm strip}\). The full rational trace kernel and
  all higher Fourier charges are unchanged.
* The initial small-height angular connector retains the old
  entire truncated wire polynomial, rather than separate
  rational currents at height zero. Its original subexponential
  cost and strict action gap absorb the polynomial insertion
  costs. The all-real-color inequality and its small complex
  enlargement are the same as in the complete source proof.

These steps are homogeneous in \(I\); normalizing by (23), or
treating \(I=0\) separately, makes the uniformity in (24) explicit.
They do not require a nonzero or slowly varying insertion. They
also show why its degree bound and the full strip norm are needed.

For the actual insertion define
\[
                  \mathfrak n_{\beta,N}(Z)
                       =\|\mathcal I_{\beta,N}(\cdot,Z)\|_{\rm strip}.
 \tag{25}
\]
The complete first-coordinate deletion theorem, its positive
rectangle estimate (26), gives
\[
 |\mathcal D_{\beta,N}^{a,\rm rt}|
       \le CN^A e^{11N/6}
 \quad\text{on}\quad
 \begin{cases}
 |Z|\le e^{3\pi/20},&\beta=0,\\
 |Z|\le1,&\beta=1.
 \end{cases}
 \tag{26}
\]
See [the sectorwise first end theorem](research_mixed_three_four_next_sectorwise_first_end.md).
This is a bound on every subset of the physical first-end rectangle,
so it is eligible for (22); it is not inferred from a full signed
coefficient bound. These disks contain all actual outputs of the
corresponding types. On the actual next-action neighborhoods its
normalized fixed jets have the cited \(1/96\) gap.

Combining (21), (24), and (26) gives the actual finite bound
\[
 \boxed{\quad
 |\mathscr R_N^{\rm cl}|
  \le C_\tau N^{A_\tau}
          e^{N(M_{\rm term}+\tau)}\mathfrak n_{\beta,N}(Z)
             +CN^A e^{11N/6}.
 \quad}
 \tag{27}
\]
Fixed ordinary derivatives have the same form with polynomial
cost. For output derivatives use the supremum of (25) on a fixed
larger output neighborhood before Cauchy's formula; no pointwise
norm alone is claimed to control those derivatives.

Equation (27) is a norm reduction, not a proof that the norm lies
below the remaining action budget. Its insertion retains the
joint \(b,j\) phases and the whole next conditional polynomial.
Even a successful bound for (27) would still have to be combined
with the explicit vertical and half-grid terms in (15) to estimate
the desired open horizontal difference.

## 5. A physical ordinary value is not a polynomial-size shortcut

The radical contraction in (18) consumes the original normal at
one traced vertex. Its remaining factor is still
\[
 \mathcal K_{3,N}(w,c_j)
   =\phi_N[\mathcal R_N^3K_N^{\rm ord}(w,\cdot)
                                      K_N^{\rm ord}(c_j,\cdot)].
 \tag{28}
\]
The low-degree spectator \(K_N^{\rm ord}(c_j,\cdot)\) is not
a radical insertion. The first normals in this terminal trace,
and the ordinary free boundary \(w\), have not disappeared.

There is an exact example already at the first physical color:
\[
 v(c_0)=\mathbf e_0,\qquad
 \mathcal K_{3,N}(w,c_0)=v(w)^TJM^3\mathbf e_0
                              =\mathcal H_{3,N}(w).
 \tag{29}
\]
This is the original complete terminal-three polynomial. Its
nonzero expansion near \(w=-2\), with positive action
\(M_{\rm term}\), is the terminal theorem cited above. Thus
the designation “physical ordinary value” cannot supply a
polynomial upper bound for all factors in (28), even at \(j=0\).
This example does not give a lower bound on the coherent insertion
(19), whose summands may cancel.

The previously paid band \(b\ge8N/9\) uses \(j<N/9\) and
an explicit terminal insertion bound; it does not cover the
full interval in (11). The new reduction preserves the wider
insertion instead of spending that restricted theorem outside its
domain. The norm (25), together with the boundary currents in
(15), is the concrete source quantity still requiring a new
comparison. No new knot-family or full-transfer assertion follows
from this reduction.
