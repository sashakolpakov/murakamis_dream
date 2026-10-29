# Closed open-port kernel of the original terminal positive packet

29 October 2026. This is an all-input formula for the terminal map in
[the complete-module positive Gram](actual_terminal_packet_positive_gram.md).
It does not substitute the figure-eight prefix. Both the recorded physical
color and the complete multiplicity input remain open. The answer consists
of finite factorial/Newton transforms and an explicit first-order factorial
Green register. Its kernel is retained.

## 1. Conventions and the open matrix

Put

\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad x=q^d,\quad
 F_a=(Q;Q)_a,\quad s_a=|F_a|,\quad \kappa=q^{d^2/2}.
\]

All factorial indices below lie between 0 and d. In particular none of
the displayed denominators vanishes. We use the original balanced heads,
coproducts, full checked crossing R, ordinary cap ell, and complete map
I_w of [the multiplicity theorem](actual_complete_source_multiplicity_module.md).
The basis of W is e_j=|j,d-j>. Thus

\[
 D(w)=I_w|d\rangle,\qquad
 T_n(w)=(\ell_{12}\otimes\langle d|)(I\otimes R^2)
                      \Pi_{\mathrm{middle}=n}D(w).                 \tag{1}
\]

The cap is \(\ell_{a,d-a}=x^{-a}Q^{-a}/N\), and R includes kappa.
This definition uses the genuine whole Hopf closure. It does not replace
an arbitrary marked coupon by an ordinary cap.

Define the finite scalar register

\[
 P_0=1,\qquad P_t=(1-Q^t)^2P_{t-1}+Q^t,
 \qquad
 P_t=F_t^2\sum_{v=0}^t\frac{Q^v}{F_v^2}.                         \tag{2}
\]

The following is the closed answer for EVERY input column j:

\[
 \boxed{\displaystyle
 T_{n,j}=(-1)^n x^{j-d}Q^{-n(n+3)/2}
       \frac{F_n}{F_{d-j}}\,
       \sum_{t=0}^{\min(n,j)}
       \frac{Q^t(Q^{-n};Q)_t(Q^{-j};Q)_t}{F_t^4}\,P_t .}         \tag{3}
\]

There is no unknown source value in this formula. In particular it
specifies the map before a preceding braid is supplied. It holds at
even, odd, prime, and composite levels.

Let V be the lower triangular finite Newton matrix
\(V_{n,t}=(Q^{-n};Q)_t\), set

\[
 D^{\mathrm{row}}_{n,n}=(-1)^nQ^{-n(n+3)/2}F_n,\qquad
 D^{\mathrm{col}}_{j,j}=x^{j-d}/F_{d-j}.
\]

Then (3) is the exact coherent congruence factorization

\[
 T=D^{\mathrm{row}}\,V\,
       \operatorname{diag}\!\left(\frac{Q^tP_t}{F_t^4}\right)
       V^{\mathsf T}D^{\mathrm{col}}.                            \tag{4}
\]

The transpose is a bilinear transpose, not an adjoint. Consequently the
diagonally rescaled kernel is symmetric. Positivity is supplied by
\(T^\dagger T\), not by declaring (4) positive.

## 2. A lowest-column crossing identity

Let A be the physical pair Casimir on W, and put
\(L=\kappa^{-1}R_{12}|_W\). Its exact entries are

\[
 L_{i,j}=\begin{cases}
 x^{-d+h}Q^{(d-j)(d-i)}
 \dfrac{F_iF_j}{F_hF_{d-j}F_{d-i}},&h=i+j-d\geq0,\\
 0,&i+j<d.
 \end{cases}                                                   \tag{5}
\]

The full lowest intertwiner column is

\[
 \boxed{\displaystyle
 D(w)=\sum_{k=0}^d\frac{F_{12}^{\,k}}{F_k}\,Lw
                         \otimes|d-k\rangle .}                 \tag{6}
\]

Here the operator F12 is distinguished from the scalar factorial F_k.
For a proof, first extract the last-color-d component of D and call
the resulting map L0. Since D is lowest for F123, its other components
are fixed by L0: on pair degree d+k+1,

\[
 K_{12}^{-1}(1-Q^{d-k})=-(1-Q^{k+1}).
\]

Thus the successive coefficients in (6) are exactly 1. There is no
omitted endpoint term: \(F_{12}^N=0\).

We next identify L0 without assuming a spectral basis. It commutes with
A because A commutes with E12, F12, and K12 in the defining highest and
lowest constructions. Let J be the actual highest-chart anti-Pascal
matrix. The already proved original source identity is

\[
 J(x^j)_{j=0}^d=e_d,\qquad J^{\mathsf T}=J.                       \tag{7}
\]

On first physical color 0 the highest column is Jw. The divided
\(F_{23}^d\) coefficient from |b,d-b> to |d,d> is x^b: expand
the two q-commuting terms and use
\(F_bF_{d-b}=N(-1)^bQ^{b(b+1)/2}\). The additional first-head
factor in F123^d is x^(-d). Hence

\[
 e_0^{\mathsf T}L_0=x^{-d}(x^b)_b^{\mathsf T}J
                   =x^{-d}e_d^{\mathsf T}.                     \tag{8}
\]

The original R commutes with A and its strict transfer formula gives
the identical first row for kappa^(-1) R. Every off-diagonal Jacobi
coefficient of A is nonzero: it is \(-(1-Q^j)^2\), 1<=j<=d.
Therefore the rows \(e_0^{\mathsf T}A^r\), 0<=r<=d, span all rows.
Two commuting maps with the same first row are equal. This proves
L0=L and (6), including all Jordan channels.

For reference, direct divided-power extraction also gives the finite
Newton/Euler expression

\[
 L=\sum_{c=0}^d
   \frac{(-1)^c q^{c(c+2)}}{F_c^2}\,F_{12}^{\,c}E_{12}^{\,c}.     \tag{9}
\]

It agrees with (5); it is not a completion of the nilpotent currents.

## 3. Forced terminal transfers and squared Pascal factorization

The total physical degree of D(w) is 2d. At recorded middle color n,
write its physical states as

\[
 (d-r,n,d-n+r),\qquad 0\leq r\leq n.
\]

The two terminal crossings and final cap force the first crossing's
transfer to n-r and the second crossing's transfer to 0. Substituting
the ORIGINAL signed-color formula, with both common Cartan factors,
gives the terminal coefficient

\[
 c_{n,r}=\frac{x^{-n}}N(-1)^{n-r}
 Q^{-n(n+1)/2-n+r(r+1)/2}\frac{F_n}{F_r}.                        \tag{10}
\]

In simplifying it we used exactly \(\kappa^2=x^d\), not a deleted
Cartan scalar. This is the only path admitted by the original finite
support for these fixed physical colors.

For a low-pair input i=d-t, the coefficient of
\(|d-r,n\rangle\) in \(F_{12}^{n-r}/F_{n-r}\) is

\[
 x^{-(n-t)}Q^{(n-t)(d-t)}
 \frac{F_{d-r}F_n}
 {F_{t-r}F_{n-t}F_{d-t}F_t},
 \qquad 0\leq r\leq t\leq n.                                 \tag{11}
\]

Multiplying (10) and (11), reflecting F_(d-r), and summing r leaves
the finite convolution

\[
 \sum_{r=0}^t\frac{Q^{r(r+1)}}{F_r^2F_{t-r}}
       =\sum_{v=0}^t\frac{Q^v}{F_v^2}
       =\frac{P_t}{F_t^2}.                                   \tag{12}
\]

A self-contained proof of the first equality is as follows. Let
E(z)=sum_r Q^{r(r+1)}z^r/F_r^2 and U(z)=sum_k z^k/F_k, as formal
series modulo z^N. Their coefficient recurrences imply

\[
 E(z)-2E(Qz)+(1-Q^2z)E(Q^2z)=0,\qquad
 U(Qz)=(1-z)U(z).
\]

For J(z)=E(z)U(z), compare coefficients through degree d to obtain

\[
 P_t=(1+Q-2Q^t+Q^{2t})P_{t-1}
           -Q(1-Q^{t-1})^2P_{t-2}.
\]

Here P_t=F_t^2[z^t]J, P0=1, P1=1-Q+Q^2. The recurrence factors
exactly: \(Z_t=P_t-(1-Q^t)^2P_{t-1}\) satisfies Z_t=Q Z_(t-1)
and Z0=1. This proves (2) and (12) at every required index.

Let Rev e_i=e_(d-i), and define

\[
 U^{(2)}_{n,t}=Q^{-nt}F_{n-t}{n\brack t}_Q^2\quad(t\leq n),
\]
\[
 D^{\mathrm{out}}_{n,n}=(-1)^nQ^{-n(n+3)/2},\qquad
 D^{\mathrm{in}}_{t,t}=(-1)^t x^tQ^{t(t+1)/2}.
\]

Both D's are unitary diagonal matrices. Equations (6), (10)--(12)
give the second useful all-exterior factorization

\[
 \boxed{\displaystyle
 T=\frac1N D^{\mathrm{out}}U^{(2)}D^{\mathrm{in}}
                    \operatorname{diag}(P_t)\,\mathrm{Rev}\,L.} \tag{13}
\]

To recover (3), use the support t<=j in (5), reflect F_(d-t), and
use

\[
 (Q^{-n};Q)_t(Q^{-j};Q)_t
   =Q^{-(n+j)t+t(t-1)}\frac{F_nF_j}{F_{n-t}F_{j-t}}.
\]

This also proves every entry of (4), rather than only its row sum.

## 4. Kernel, open Gram, and exact angle incidence

All matrices flanking diag(P) in either (4) or (13) are invertible.
Consequently

\[
 \operatorname{rank}T=\#\{t:P_t\ne0\},\qquad
 \ker T=L^{-1}\mathrm{Rev}\,
                  \operatorname{span}\{e_t:P_t=0\}.             \tag{14}
\]

For N=6, Q^2-Q+1=0, the successive values P0,...,P5 are

    1, 0, Q-1, 4Q-5, -4Q-12, 17-13Q.

Thus the actual complex packet has rank 5. The positive completion in
the terminal Gram note is essential; an inverse of T would be invalid.
No lower bound on nonzero P_t is assumed here. The elementary uniform
upper bound |P_t|<=(4^(t+1)-1)/3 follows from (2), but is not sharp.

For every input w, not only a specified knot prefix, (13) gives the
SOURCE-EXACT positive energy

\[
 \sum_n|T_nw|^2=\frac1{N^2}\sum_n
   \left|\sum_{t\leq n}U^{(2)}_{n,t}
       D^{\mathrm{in}}_{t,t}P_t(Lw)_{d-t}\right|^2.             \tag{15}
\]

All interference between distinct t is retained. Equivalently the
open Gram is

\[
 T^\dagger T=\frac1{N^2}L^\dagger\mathrm{Rev}\,
  \operatorname{diag}(\bar P) (D^{\mathrm{in}})^\dagger
  (U^{(2)})^\dagger U^{(2)}D^{\mathrm{in}}
  \operatorname{diag}(P)\mathrm{Rev}\,L.                       \tag{16}
\]

This is an explicit finite matrix on the original complete module.
Neither dephasing the t register nor dropping its P_t multiplier
preserves (15) in general.

There is also a genuine local angle weight, with its metric fully
specified. For k=n-t and
\(w_d(a,b,c)=1/(s_as_bs_c)\), define the THREE-PORT tensor

\[
 \widetilde U_{n;t,k}=\delta_{n,t+k}\,
       s_n^{-3/2}s_t^{3/2}s_k^{1/2}U^{(2)}_{n,t}.
\]

The exact reflection identity gives

\[
 \boxed{\displaystyle
 \frac1N|\widetilde U_{n;t,k}|^2
       =w_d(t,k,d-n),\qquad t+k+(d-n)=d.}                      \tag{17}
\]

Its phase is the ACTUAL phase of
\(Q^{-nt}F_{n-t}{n\brack t}_Q^2\). The factors
\(s_n^{-3/2}s_t^{3/2}s_k^{1/2}\) are recorded length metrics;
they cannot be applied to the two matrix ports while silently deleting
the k port or the adjacent source metric. In terms of the existing
length gauge A_a=(s_a^2/N)^(1/8), this factor is
\(N^{1/4}A_n^{-6}A_t^6A_k^2\). Length zero has s0=1 and is retained.

Thus the open packet contains a precise angle-simplex tensor and a
coherent original factorial Green register. This is not a proof that
every full packet energy is a geometric angle partition function:
the complete prefix Lw, the P register, and the exterior length
metrics still have to be controlled together.

## 5. Scope and audit

The construction applies to arbitrary original prefixes and to arbitrary
vectors in the complete W at the selected cut. It is not restricted to
the one Casimir source plane. It proves a closed formula and a coherent
energy identity; it does not prove a sharp broad-knot upper estimate.
The known identity T_n(R12^(-1)R23 p)=|F_n|^2 is an additional
prefix-specific cancellation, not a definition of this T.

[Audit](../experiments/audit_actual_terminal_packet_closed_kernel.py)
constructs H, D, the two terminal original crossings, and their full
physical projectors directly from the original generators. It compares
every input column with (3), (6), (9), and (13); checks the exact rank
and shifted-Durfee/Green identities; and verifies the literal angle
metrics separately over the complex principal roots.

Fresh replay: PASS ten complete original open matrices at N=2,...,10,12,
including every input column, original row-sum source and benchmark
packet; eleven complex-root three-port angle-metric families.

The [quantitative Green companion](actual_terminal_green_capacity_bound.md)
combines the Pascal phases into the simpler exact form
T=N^(-1)diag(x^n)R diag(P_(d-j))R. It uses the actual polynomial
endpoint P_d to control all Green colors, and proves a one-crossing
capacity bound for T R^(-1) with an arbitrary preceding input. It
does not establish a broad sharp knot-volume bound.
