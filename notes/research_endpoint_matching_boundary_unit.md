# Endpoint-current matchings are units in the full boundary algebra

Private research note, 15 November 2026.

The exact simultaneous endpoint-current polynomial has no zero at any
physical assignment of its remaining boundary variables, for every
level \(N\ge3\) and every choice of signed current powers, except when
one of its even powers is zero. More strongly, its inverse retains all
mixed first Hermite normals with a polynomial bound uniform in those
powers. This follows from an accretive determinant for the actual
current coefficients.

This is a finite boundary-algebra statement. It does not give a lower
bound after the prescribed exterior trace, nor identify a selected
geometric coefficient of the original scalar. The earlier matching
theorem already proves a nonzero leading current coefficient when a
complete exterior contour theorem is supplied. The result here requires
no such contour theorem.

## 1. The actual polynomial and its determinant

Use the original notation
\[
 D=N-1,\quad \eta=(-1)^D,\quad \sigma=(-1)^N=-\eta,\quad
 \theta=\pi/N,\quad c_0=2\cos\theta,\quad
 s_1=2\sin\theta,\quad \rho=i s_1.
 \tag{1}
\]
Let \(G\) be a finite circle tree, \(S\) a subset of its vertices,
and \(n_v\in\mathbb Z\) the signed one-step Ward-current power at
\(v\in S\). Let \(O\subset S\) be its odd-power vertices and
\(E=S\setminus O\). The remaining boundary variables are \(w_j\),
indexed by the outside vertices adjacent to \(S\); write their set
as \(B\), with \(b=|B|\).

Put \(U_N=T\Pi_0\), the original turned full endpoint idempotent.
Let \(m_{vj}\) be the number of actual incidences from \(v\) to
outside vertex \(j\), and \(d_v=\sum_jm_{vj}\). For a simple tree
these numbers are zero or one, but their incidence notation keeps
shared outside variables explicit. The exact monomers are
\[
 A_v(\mathbf w)=
 \begin{cases}
  \sigma n_vN\rho,&v\in E,\\[1mm]
  2\sum_jm_{vj}U_N(w_j)
       +\eta\{n_v\rho+2(d_v-1)c_0\},&v\in O,
 \end{cases}
 \qquad d_N=\frac{s_1^2(N^2-1)}3>0.
 \tag{2}
\]
The full boundary polynomial of these inserted currents is exactly
\[
 \mathcal E_{S,N}(\mathbf w)
   =\sum_{\substack{M\subset E(G[O])\\M\ {\rm matching}}}
      d_N^{|M|}\prod_{v\in S\setminus V(M)}A_v(\mathbf w).
 \tag{3}
\]
This is Theorem 1 of the
[grouped endpoint-current note](research_grouped_endpoint_current_matchings.md).
It is an ordinary polynomial identity before any boundary reduction;
every internal mixed first normal and every actual outside incidence
is retained.

If any \(v\in E\) has \(n_v=0\), (3) is identically zero. Henceforth
assume all even powers are nonzero. Define
\[
 B_E=\prod_{v\in E}\sigma n_vN\rho,\qquad
 m=|O|,\qquad x_v=\sigma A_v\quad(v\in O),
 \qquad
 \mathsf D(\mathbf w)=\operatorname{diag}(x_v)
               +i\sqrt{d_N}\,\operatorname{Adj}(G[O]).
 \tag{4}
\]
Empty determinants and products equal one. Then
\[
                 \boxed{\ \mathcal E_{S,N}
                      =B_E\,\sigma^m\det\mathsf D.\ }
 \tag{5}
\]
Indeed a permutation supported by a forest has only fixed points
and edge transpositions. A transposition contributes
\(-[i\sqrt{d_N}]^2=d_N\). Factoring \(\sigma\) from each unmatched
odd monomer contributes \(\sigma^{m-2|M|}=\sigma^m\), proving (5).
No sum over physical colors or contraction of the exterior has been
taken in this determinant.

For any complex boundary assignment satisfying
\(\Re x_v>0\) at every odd vertex, write
\[
 \mathsf D=\mathsf R+i\mathsf H,\qquad
 \mathsf R=\operatorname{diag}(\Re x_v)>0,\qquad
 \mathsf H=\operatorname{diag}(\Im x_v)
               +\sqrt{d_N}\operatorname{Adj}(G[O]).
 \tag{6}
\]
The matrix \(\mathsf H\) is Hermitian. Therefore
\[
 |\det\mathsf D|
  =\det\mathsf R\,
    \left|\det\!\left(I+i\mathsf R^{-1/2}
                         \mathsf H\mathsf R^{-1/2}\right)\right|
  \ge\prod_{v\in O}\Re x_v,
 \qquad
 \|\mathsf D^{-1}\|\le(\min_v\Re x_v)^{-1}.
 \tag{7}
\]
The determinant inequality follows from the real eigenvalues of
\(\mathsf R^{-1/2}\mathsf H\mathsf R^{-1/2}\).
For the inverse estimate, Cauchy--Schwarz and
\(\Re\langle u,\mathsf Du\rangle\ge
(\min\Re x_v)\|u\|^2\) give the least-singular-value bound.

## 2. Every physical boundary assignment is in this sector

Let
\[
 c_a=2\cos((2a+1)\theta),\qquad
 0\le a\le\lfloor D/2\rfloor
 \tag{8}
\]
be the distinct physical nodes. All are double except the last node
\(-2\) when \(N\) is odd. The exact full Ward-coupon formulas are
\[
 \begin{split}
 \sigma U_N(c_a)
   &=c_0+2\sin\theta\sum_{r=1}^a\cot(r\theta),\\
 U_N'(c_a)
   &=-\sigma\frac{\sin\theta}{4\sin((2a+1)\theta)}
                  \sum_{r=a+1}^{N-1-a}\csc^2(r\theta)
                     \quad\text{at double nodes}.
 \end{split}
 \tag{9}
\]
These are equations (21)--(22) of the
[signed Ward note](research_signed_gaussian_ward_endpoint_packet.md).
The first formula includes the odd simple node. Every cotangent
in it is positive, unless the sum is empty.

At an arbitrary physical outside assignment
\(\mathbf c=(c_{a_j})_{j\in B}\), (2) and (9) give, for \(v\in O\),
\[
 \begin{split}
 x_v(\mathbf c)&=r_v(\mathbf c)-i n_vs_1,\\
 r_v(\mathbf c)
  &=2c_0+
     4\sin\theta\sum_jm_{vj}\sum_{r=1}^{a_j}\cot(r\theta)
       \ \ge\ 2c_0.
 \end{split}
 \tag{10}
\]
In particular all powers affect only the imaginary parts of these
odd monomers. For \(N\ge3\), put
\(\delta_N=2c_0=4\cos(\pi/N)\ge2\).
Equations (5), (7), and (10) prove the exact bound
\[
 \boxed{\quad
 |\mathcal E_{S,N}(\mathbf c)|
 \ge
    (Ns_1)^{|E|}\!\left(\prod_{v\in E}|n_v|\right)
       \prod_{v\in O}r_v(\mathbf c)
 \ge
    (Ns_1)^{|E|}\!\left(\prod_{v\in E}|n_v|\right)
       \delta_N^m>0 .
 \quad}
 \tag{11}
\]
This holds simultaneously for all assignments, all signed integer
powers, and both level parities. Powers may even depend on \(N\).
Restoring the original common crossing units \(\kappa_N^{n_v}\)
does not change (11), since those units have modulus one.

The restriction \(N\ge3\) is necessary. At \(N=2\), two adjacent
odd current vertices with no exterior and powers \(n_1=n_2=1\)
have \(A_1=A_2=-2i\) and \(d_N=4\), so (3) is exactly zero.
This is a degeneracy of the actual current polynomial, not an
asymptotic example.

## 3. Inversion retains every mixed first normal

Let
\[
 \mathcal A_N=\mathbb C[w]/(2T_N(w/2)+2),\qquad
 \mathcal B_N=\bigotimes_{j\in B}\mathcal A_N.
 \tag{12}
\]
Use its full Hermite seminorm
\[
 \|f\|_{\mathcal J,B}
   =\max_{\mathbf c,J}
       |\partial_J f(\mathbf c)|,\qquad
 \partial_J=\prod_{j\in J}\partial_{w_j},
 \tag{13}
\]
where \(J\subset B\) contains only variables assigned to double
nodes; each variable is differentiated at most once. These are
all local tensor-algebra coordinates, so (13) is a norm on
\(\mathcal B_N\).

**Theorem.** Under the hypotheses of (11), the class of
\(\mathcal E_{S,N}\) is a unit of \(\mathcal B_N\).
For every allowed \(J\), \(r=|J|\), its inverse satisfies
\[
 \boxed{\quad
 |\partial_J\mathcal E_{S,N}^{-1}(\mathbf c)|
 \le
  \frac{1}{(Ns_1)^{|E|}\prod_{v\in E}|n_v|}
  \,\delta_N^{-m-r}(m)_r
  \prod_{j\in J}\frac{M_j(N^2-1)}6 ,
 \quad}
 \tag{14}
\]
where \(M_j=\max_{v\in O}m_{vj}\), with \(M_j=0\) if \(O\) is empty,
\((m)_0=1\), and
\((m)_r=m(m+1)\cdots(m+r-1)\) for \(r>0\).
If \(O\) is empty, its positive-order inverse derivatives vanish.
In particular there is a constant depending only on the fixed
incidence pattern such that
\[
                \|\mathcal E_{S,N}^{-1}\|_{\mathcal J,B}
                         \le C_{G,S}N^{2b}.
 \tag{15}
\]
The constant is independent of all current powers.

**Proof.** The Chinese remainder decomposition of (12) is a product
over physical assignments of rings
\[
           \mathbb C[\epsilon_j:j\ {\rm double}]
                         /(\epsilon_j^2:j\ {\rm double}).
 \tag{16}
\]
An element in any such ring is a unit precisely when its constant
coefficient is nonzero. Equation (11) proves that condition at
every assignment. Its inverse data are those of the analytic
function \(1/\mathcal E_{S,N}\) near each assignment.

For the quantitative assertion, the normal formula (9) implies
\[
 |U_N'(c_a)|\le\frac{N^2-1}{12}.
 \tag{17}
\]
Indeed \(\sin((2a+1)\theta)\ge\sin\theta\) at the double nodes,
and \(\sum_{r=1}^{N-1}\csc^2(r\theta)=(N^2-1)/3\).
Consequently
\[
 \mathsf D_j:=\partial_{w_j}\mathsf D
       =2\sigma\,\operatorname{diag}(m_{vj}U_N'(c_{a_j})),
 \qquad
 \|\mathsf D_j\|\le M_j(N^2-1)/6.
 \tag{18}
\]
Every mixed derivative of \(\mathsf D\) in two distinct boundary
variables is zero. Its possibly nonzero pure higher derivatives
are never used by (13).

Choose any local logarithm \(h=\log\det\mathsf D\) near the
assignment. For a nonempty set \(J\) of \(r\) distinct variables,
the expansion of
\(\operatorname{tr}\log(I+\mathsf D^{-1}\Delta\mathsf D)\)
gives
\[
 \partial_J h
  =\frac{(-1)^{r-1}}r
      \sum_{\pi\in\operatorname{Perm}(J)}
       \operatorname{tr}
       (\mathsf D^{-1}\mathsf D_{\pi_1}\cdots
        \mathsf D^{-1}\mathsf D_{\pi_r}).
 \tag{19}
\]
Only terms linear in each distinct increment contribute.
By (7), (10), and the dimension \(m\),
\[
             |\partial_Jh|
       \le m(r-1)!\,\delta_N^{-r}
                              \prod_{j\in J}\|\mathsf D_j\|.
 \tag{20}
\]
The repeated product rule for \(e^{-h}\) is
\[
 \partial_J e^{-h}
   =e^{-h}\sum_{\mathcal P\ {\rm partition\ of}\ J}
                       \prod_{C\in\mathcal P}(-\partial_Ch).
 \tag{21}
\]
The sum of the corresponding absolute combinatorial weights is
\[
 \sum_{\mathcal P}m^{|\mathcal P|}
                 \prod_{C\in\mathcal P}(|C|-1)!=(m)_r.
 \tag{22}
\]
For positive integer \(m\), the left side counts permutations of
\(J\) with one of \(m\) colors on every cycle. Adding the next
element either starts a colored singleton in \(m\) ways or inserts
it after one of the previous elements; this gives the displayed
rising product. The empty-set case has value one.

Now \(|\det\mathsf D|^{-1}\le\delta_N^{-m}\) by (7).
Multiply (21) by the constant \((B_E\sigma^m)^{-1}\) and use
(18)--(22). This gives (14). Finally
\(\delta_N\ge2\), \(Ns_1=2N\sin(\pi/N)\ge4\),
and \(|n_v|\ge1\) for every even current. Since \(r\le b\)
and the graph is fixed, (15) follows. \(\square\)

Thus multiplication by the current is injective on the *full*
boundary algebra, not merely on its semisimple quotient. For any
boundary state \(f\), the ordinary product rule and (15) give
\[
      \|f\|_{\mathcal J,B}
       \le 2^b C_{G,S}N^{2b}
                    \|\mathcal E_{S,N}f\|_{\mathcal J,B}.
 \tag{23}
\]
For fixed powers the forward multiplier also has polynomial
Hermite norm: the Ward coupon in (9) has values
\(O(1+\log N)\) and first normals \(O(N^2)\), and (3) has a
fixed number of factors.
Consequently current multiplication preserves the exponential
rate of this boundary norm in both directions for fixed powers.

## 4. What this does and does not control

The theorem applies to the specified simultaneous one-step endpoint
currents in their original slots. It does not identify an arbitrary
relative-contour remainder with those currents. Shared outside
variables, all unchosen edges, the retained boundary polynomial, and
the original exterior contraction remain exactly where (3) places
them.

In particular, for the prescribed exterior functional \(\Lambda_N\),
\[
          \Lambda_N(\mathcal E_{S,N}f)
 \tag{24}
\]
may vanish even though \(\mathcal E_{S,N}\) is a unit and \(f\ne0\).
Equations (11), (15), and (23) do not supply a scalar lower bound
for (24), a nonzero original contour intersection, or a certificate
for the ideal of all geometric scalar coefficients.

The pointwise complex criterion is exactly the sufficient condition
\(\Re x_v>0\) used in (6). No positive-period hypothesis was needed
to prove it on the physical grid. It has not been deduced for the
canonical boundary polynomial at an arbitrary complex geometric
evaluation. Agreement of a different representative's physical
Hermite data does not establish its equality as an ordinary
polynomial at that evaluation, or a zero-free inverse throughout
an entire complex physical window.

Section 3 of the earlier grouped-current note treats a different
question: when the complete exterior contour and all its currents
are already controlled, the logarithmic Ward representative gives a
nonzero leading matching coefficient relative to that exterior
packet. The present exact finite unit and uniform inverse-normal
bound do not assume that result's contour hypotheses, and do not
remove them from its scalar conclusion.

## 5. Direct sources and written verification

The proof uses the following two direct sources. Their complete
written proofs were read; their recorded computational checks are
not used here.

| Source | Direct implication | SHA256 |
|---|---|---|
| [Grouped endpoint currents](research_grouped_endpoint_current_matchings.md) | Equations (2)--(10): actual simultaneous current, incidence monomers, positive edge weight, exact full-boundary matching identity; Section 3 for the stated prior scope | \(\texttt{4047782f665e9e6631e73aac42d55057d6f3cd5ae1e813d89111a0a5caaa21bb}\) |
| [Signed Gaussian Ward packet](research_signed_gaussian_ward_endpoint_packet.md) | Equations (21)--(23): exact physical values, confluent first normals, odd simple node and quadratic normal bound | \(\texttt{6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191}\) |

All deductions above are written algebra and estimates. No
mathematical execution, numerical evidence, or tests are used.
