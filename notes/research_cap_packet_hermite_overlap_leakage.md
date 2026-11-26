# One overlapping crossing leaves the cap packets and both local source planes

20 November 2026. This note concerns an exact three-head interface. It
does not concern a particular knot. The normalized ordinary-cap packets
are coisometric, and the cup channel has a well-conditioned two-dimensional
Hermite frame. Nevertheless, their sum is not preserved by the adjacent
original crossing. A bounded finite-difference operator detects the part
that leaves this sum. For every \(N\geq32\), its squared norm is at
least \(1/128\) of the squared norm of the entire crossed packet.

The conclusion is about this specified packet compression. It does not
exclude a larger packet system, a coupled metric depending on the gluing,
or cancellation under the original closing functional.

## 1. The three actual maps used here

Fix an integer \(N\geq2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 x=q^d=-q^{-1},\qquad
 F_a=\prod_{r=1}^a(1-Q^r),\qquad s_a=|F_a|.
\]
Empty products are one. Let \(V=\mathbb C^N\), with basis
\(|a\rangle\), \(0\leq a\leq d\), and write
\(\mathcal H=V^{\otimes3}\). All adjoints, distances and orthogonal
projections below use the Euclidean inner product in the specified
gauged physical coordinates.

The quarter factorial gauge on one head is
\[
 B_a=N^{1/4}s_a^{-1/2}.
\]
Root complementation gives
\[
 F_aF_{d-a}=N(-1)^aQ^{a(a+1)/2},\qquad
 s_as_{d-a}=N,\qquad B_aB_{d-a}=1.                    \tag{1}
\]
In particular the gauge is the identity on every physical two-head
degree-\(d\) subspace. It does not change the cup, either original cap
on that subspace, or the degree-\(d\) crossing matrix used below.

The complete ordinary-cap node in
[the cap-tree theorem](actual_cap_tree_angle_energy.md), Section 1,
is the actual pivotal-cap reassociation map
\[
 \widehat K_{n;(a,b,c)}
 =\delta_{b,d}\delta_{n=a+c\leq d}
 q^{a(n-N-1)}\frac{1}{\sqrt{s_as_cs_{d-n}}}.          \tag{2}
\]
Its row energies are
\[
 E_{2,n}=\frac{s_n}{N}\sum_{a+c=n}\frac1{s_as_c},
 \qquad
 \mathcal R=\operatorname{diag}(E_{2,n}^{-1/2})\widehat K,
 \qquad \mathcal R\mathcal R^*=I_V.                  \tag{3}
\]
Here \(\mathcal R\) denotes the cap coisometry, not a braid crossing.
Let \(\mathcal C=\operatorname{ran}\mathcal R^*\). Every vector in
\(\mathcal C\) is supported on middle index \(b=d\). Since
\(E_{2,0}=1/N\), its root-zero packet is exactly
\[
 u=\mathcal R^*|0\rangle=|0,d,0\rangle,
 \qquad \|u\|=1.                                    \tag{4}
\]
Thus no arbitrary input vector has been chosen in place of a cap packet.

We also retain the full actual cup Hermite plane on either neighboring
pair. On \(W=(V\otimes V)_{\mathrm{degree}\ d}\), write
\[
 g_a=x^{a-d},\qquad
 H_a=\sum_{r=1}^a\frac1{1-Q^r},\qquad
 \rho=q-q^{-1},\qquad
 v_a=-g_aH_a/\rho.
\]
The source-plane theorem
[with the original cup and caps](actual_tame_c0_hermite_source_frame.md),
Sections 1--3, gives
\[
 \mathcal S=\operatorname{span}(p,t_N)
           =\operatorname{span}(g,gH),\qquad p=Ng,     \tag{5}
\]
where \(t_N=(v-\mu_Np)/\gamma_N\),
\(\gamma_N=(-1)^N/(N\rho^2)\ne0\). In this plane the *original*
marked and ordinary rows are
\[
 m_a=x^{d-a}/N^2,\qquad \ell_a=x^{-a}Q^{-a}/N,
\]
and obey
\[
 mp=1,\quad mt_N=0,\quad \ell p=0,\quad \ell t_N=1.
                                                               \tag{6}
\]
Consequently \(|mz|^2+|\ell z|^2\) is the source Hermite norm.
The derivative vector \(t_N\) is included throughout this note.
The ordinary cap has not replaced the marked cap. No assertion is made
about extending the displayed restriction of the marked row to other
pair degrees.

Let \(\mathcal S_{12}\otimes V\) and
\(V\otimes\mathcal S_{23}\) mean the literal embeddings of (5) on
the indicated neighboring heads, with the remaining head unrestricted.
Our enlarged packet space is
\[
 \mathcal E=\mathcal C+
       (\mathcal S_{12}\otimes V)+(V\otimes\mathcal S_{23})
       \subseteq\mathcal H.                          \tag{7}
\]
This is a sum of subspaces, with their actual intersections. In
particular no separate squared coefficient norm is imposed on its
possibly redundant spanning columns.

## 2. The full adjacent crossing on the selected packet

Write \(R_+\) for the original positive checked crossing, including
its common Cartan scalar \(\kappa=q^{d^2/2}\). Section 2, equation (5),
of [the complete open terminal kernel](actual_terminal_packet_closed_kernel.md)
gives its literal degree-\(d\) block. For input \(|d,0\rangle\),
its \(|a,d-a\rangle\) coefficient is
\[
 (R_+)_{a,d}=\kappa x^{a-d}\frac{N}{F_{d-a}}.
\]
Using (1) and
\[
 \overline{F_a}=(-1)^aQ^{-a(a+1)/2}F_a
\]
therefore gives the exact vector
\[
 w=(I\otimes R_+)u
   =\kappa\sum_{a=0}^d g_a\overline{F_a}\,|0,a,d-a\rangle.
                                                               \tag{8}
\]
The sign, conjugation and Cartan factor in (8) have all been retained.
The gauge in (1) does not change (8): heads 2 and 3 have total degree
\(d\), and the unchanged first-head gauge cancels between input and
output. In particular
\[
 \|w\|^2=Z_N:=\sum_{a=0}^d s_a^2.                   \tag{9}
\]

Even before adjoining the Hermite planes, the orthogonal cap-packet
projection is explicit. Its only overlap with the support of (8) is
\(|0,d,0\rangle=u\). Thus
\[
 P_{\mathcal C}w=\kappa N u,\qquad
 \|(I-P_{\mathcal C})w\|^2=Z_N-N^2.                \tag{10}
\]
Equation (10) uses the complete cap-packet projection, including the
coherent entries of every root row.

## 3. A row annihilating the cap packets and both Hermite planes

For an integer \(j\) with \(1\leq j\) and \(j+2\leq d-1\), put
\(A_r=1-Q^r\). Define the complex-linear row on \(\mathcal H\)
by
\[
\begin{split}
 L_j(z)={}&A_{j+2}\left(
   \frac{z_{0,j+2,d-j-2}}{g_{j+2}}
  -\frac{z_{0,j+1,d-j-1}}{g_{j+1}}\right)\\
 &-A_{j+1}\left(
   \frac{z_{0,j+1,d-j-1}}{g_{j+1}}
  -\frac{z_{0,j,d-j}}{g_j}\right).
\end{split}                                                   \tag{11}
\]
Because \(|g_a|=1\) and \(|A_a|\leq2\), its squared Euclidean dual
norm satisfies
\[
 \|L_j\|_*^2
 =|A_{j+2}|^2+|A_{j+2}+A_{j+1}|^2+|A_{j+1}|^2
 \leq24.                                                \tag{12}
\]

**Lemma.** The row \(L_j\) annihilates all of \(\mathcal E\), and
\[
 L_j(w)=-\kappa Q^{-j-2}\overline{F_{j+1}}.             \tag{13}
\]

*Proof.* Every coefficient sampled in (11) has middle index at most
\(d-1\). It therefore vanishes on \(\mathcal C\), whose middle
index is \(d\). On \(\mathcal S_{12}\otimes V\), a nonzero sampled
coefficient with first head zero would require the second head to be
\(d\), since that source pair has degree \(d\). These coefficients
also vanish.

On \(V\otimes\mathcal S_{23}\), the sampled quotient by \(g_a\)
has the form \(\alpha+\beta H_a\), for some \(\alpha,\beta\)
depending on its first-head-zero coefficient. The two weighted
differences in (11) are both \(\beta\), because
\[
 A_r(H_r-H_{r-1})=1.
\]
Their difference is zero. This proves the annihilation of the full
sum (7), with its derivative channels and all cross terms retained.

Finally set \(f_a=\overline{F_a}\). Its actual consecutive-factor
recurrence gives
\[
 f_r=(1-Q^{-r})f_{r-1},\qquad
 A_r(f_r-f_{r-1})=f_r.
\]
Substitute (8) in (11). The result is
\(\kappa(f_{j+2}-f_{j+1})=-\kappa Q^{-j-2}f_{j+1}\),
which is (13). \(\square\)

Let \(P_{\mathcal E}\) be the actual orthogonal projection onto
the sum (7). The lemma and Cauchy--Schwarz now prove the finite bound
\[
 \boxed{\quad
 \|(I-P_{\mathcal E})w\|^2
 \geq\frac{s_{j+1}^2}{24}.
 \quad}                                                   \tag{14}
\]
Indeed \(L_j(w)=L_j((I-P_{\mathcal E})w)\). All sampled factorials
are nonzero. Thus (14) already proves failure of invariance whenever
the indicated three interior indices exist, namely \(N\geq5\).
It does not rely on an asymptotic estimate.

The same calculation is stronger when all these rows are retained
together. Let \(\mathcal Lz=(L_j(z))_{j=1}^{d-3}\), and extract the
length-\(N\) slice
\(f_a=z_{0,a,d-a}/g_a\). The extraction has norm one. The forward
difference map \((\Delta f)_r=f_r-f_{r-1}\), \(1\leq r\leq d\),
has norm at most two. Multiplication by \(A_r\) has norm at most
two, and the second difference has norm at most two. Restricting
its output to the indicated rows does not increase the norm. Thus
\[
 \|\mathcal L\|\leq8,\qquad \mathcal L|_{\mathcal E}=0,
 \qquad
 \|\mathcal Lw\|^2=\sum_{k=2}^{d-2}s_k^2.             \tag{15}
\]
For every \(N\geq5\), the four omitted indices \(0,1,d-1,d\)
are distinct. Define
\[
 B_N=1+s_1^2+s_{d-1}^2+N^2.
\]
Equations (9) and (15) prove the exact finite bound
\[
 \boxed{\quad
 \|(I-P_{\mathcal E})w\|^2\geq\frac{Z_N-B_N}{64},
 \qquad B_N\leq5+N^2+\frac{N^4}{16}.
 \quad}                                                   \tag{16}
\]
For the last inequality use \(s_1\leq2\),
\(s_{d-1}=N/s_1\), and \(s_1=2\sin(\pi/N)\geq4/N\).

This gives a fixed fraction without invoking an exponential
asymptotic. The included term \(s_{d-2}^2\) satisfies
\[
 Z_N\geq s_{d-2}^2=\frac{N^2}{s_2^2}
 \geq\frac{N^6}{64\pi^4},
 \qquad s_2=4\sin(\pi/N)\sin(2\pi/N)
          \leq\frac{8\pi^2}{N^2}.
\]
Consequently
\[
 \frac{\|(I-P_{\mathcal E})w\|^2}{Z_N}
 \geq\frac1{64}\left[
 1-64\pi^4\left(\frac5{N^6}+\frac1{N^4}
                                      +\frac1{16N^2}\right)\right].
                                                               \tag{17}
\]
In particular the ratio is at least \(1/128\) for every
\(N\geq32\). Indeed \(\pi^4<100\), \(5/N^6\leq1/N^4\),
and
\(6400(2/32^4+1/(16\cdot32^2))=211200/524288<1/2\).
The correction term in (17) is \(O(N^{-2})\).

## 4. The leakage has the full factorial exponential rate

Define the Lobachevsky function and regular ideal tetrahedron volume by
\[
 \Lambda(\theta)=-\int_0^\theta\log(2\sin t)\,dt,
 \qquad v_3=3\Lambda(\pi/3).
\]
With \(J(t)=\int_0^t\log(2\sin\pi r)\,dr\), the elementary
uniform sine-factorial estimate is
\[
 \log s_a=NJ(a/N)+O(\log N),\qquad 0\leq a\leq d.     \tag{18}
\]
For completeness, subtract \(\log t+\log(1-t)\) from
\(\log(2\sin\pi t)\). The remainder extends to a continuously
differentiable function on \([0,1]\), so its Riemann-sum error is
bounded uniformly in the upper endpoint. Integral comparison for
each of the two logarithms gives an \(O(\log N)\) error, uniformly
for every integer upper endpoint \(a\). This proves (18), including
\(a=0,d\).

The unique global maximum of \(J\) is at \(5/6\). Its derivative
is negative on \((0,1/6)\), positive on \((1/6,5/6)\), and
negative on \((5/6,1)\); also \(J(0)=J(1)=0\). Moreover
\[
 J(5/6)=\frac{\Lambda(\pi/6)}\pi=\frac{v_3}{2\pi}.
\]
Here \(\Lambda(\pi-\theta)=-\Lambda(\theta)\), and the duplication
identity at \(\theta=\pi/6\) gives
\(2\Lambda(\pi/6)=3\Lambda(\pi/3)=v_3\). These are identities of
the displayed integral, not an assumption about a knot volume.

Bounding the positive sum in (9) by \(N\max_a s_a^2\), and using
the term \(a=\lfloor5N/6\rfloor\) for its lower bound, proves
\(\log Z_N=Nv_3/\pi+O(\log N)\) from (18). The fixed-fraction
lower bound (17) now gives
\[
 \boxed{\qquad
 \log\|(I-P_{\mathcal E})(I\otimes R_+)\mathcal R^*|0\rangle\|^2
 =\frac{v_3}{\pi}N+O(\log N)
 =\log\|w\|^2+O(\log N).
 \qquad}                                                   \tag{19}
\]
The constants are independent of \(N\). The stronger finite statement
(17) says that the escaping part occupies a definite fraction of the
full energy, rather than merely having its exponential rate.

## 5. What this settles about the proposed orthogonality

Let \(S\) be any synthesis map whose columns span precisely
\(\mathcal E\). Its correct coefficient Gram is \(S^*S\), including
all off-diagonal entries and all exact dependencies. Formula (14)
says that \(w\) is outside its range. Consequently no coordinate
operator \(A\) on those columns can satisfy
\((I\otimes R_+)S=SA\) on every column: the root-zero cap packet
(4) already contradicts such an identity. Using the exact Gram is
necessary, but it cannot make these specified columns into a complete
overlapping-gluing packet system.

The Hermite planes in (7) are the full local planes, with the actual
marked and ordinary rows (6). Thus the failure is not caused by
discarding the repeated-root derivative. It is caused by other
physical channels generated by an adjacent crossing. The present
argument does not identify those additional channels with null
directions of a whole-knot closing row. In particular it gives no
lower bound on a closed invariant.

The cap simplex in (2)--(3) remains valid. At its root-zero row the
only simplex charges are \((0,0,d)\), and its unnormalized row
energy is \(1/N\). That existing row weight does not account for
the new factorial rate in (19). A geometric energy argument using
these packets must therefore retain and allocate the additional
crossing channels. This note supplies neither an incidence map to
the edge equations of an ideal triangulation nor a Casson--Rivin
optimization theorem for that enlarged system.

All statements tensor with a spectator Hilbert space: tensor the
vectors with a unit spectator and the detecting row with its adjoint.
This is an all-exterior interface statement. It does not assert that
the selected input is reached by an unspecified original knot prefix.

## 6. Direct dependencies and written review scope

The author read each of the following complete files, including the
printed proofs and limitations. Their SHA-256 hashes at the end of the
author's proof check are:

| Direct source | SHA-256 |
|---|---|
| [Complete cap-tree theorem](actual_cap_tree_angle_energy.md) | `ecaf7177962dfa5a944a532fed37d505b97e81361926039f69cbf7f9b674a2da` |
| [Original source Hermite frame](actual_tame_c0_hermite_source_frame.md) | `626bc46c92e4abf1b20ffbe63267cfd78d55c28d4cc36fc64686829f93def012` |
| [Complete open terminal kernel](actual_terminal_packet_closed_kernel.md) | `ad52ab424c4d9b26e8074ec9a8391e7d48a360e10d23a2ad73248fb516a5fc2c` |

The new claim is the explicit row (11), its annihilation of the sum
(7), the bounded combined difference operator (15), and the
quantitative leakage theorem (16)--(19). The direct
sources state the possibility of adjacent-channel leakage but do not
give this calculation after adjoining both local source Hermite
planes. This note uses written finite identities and integral
estimates only. No mathematical program, experiment, test, build or
numerical sample was used in its proof check.
