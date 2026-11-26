# The top-column integral and a bounded observer of the original source

Private written proof, 19 November 2026.

The off-diagonal top column of physical highest-block completion
contains the original pointed source through a literal physical
corner and the remaining pivot. Its observer has polynomial norm
at fixed width. The triangular lowering frame cancels from this
observer exactly, so its exponential condition number is not paid.
The formula holds throughout the stated fixed-root meridian collars
and retains every true meridian derivative.

This is one prescribed bilinear contraction of the top column.
It does not give a lower bound for that contraction from the norm
of the full column, or a nonzero geometric period coefficient.
The complete directs H and L are pinned below.

## 1. Actual spaces, endpoints, and normalization

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
Keep this root fixed while varying
\[
 M=e^\mu,\quad x=-M/q,\quad
 e_a=MQ^{-a}-M^{-1}\quad(1\le a\le d),\quad
 \eta_d=\prod_{a=1}^d e_a.
 \tag{1}
\]
There are \(m=r+1\) heads, with \(r\ge1\). Let \(U\) be the
remaining \(r\)-head tensor, with its actual ordered \(E,F,K\).
As in H, let \(H\in\operatorname{End}(U)\) commute with \(K\)
and let \(W_H\) be its unique total intertwiner with physical
highest block \((W_H)_{00}=H\). Write
\[
 C_a=(W_H)_{a0},\qquad g=K^{-d},\qquad
 \Phi_0(W_H)=\tau(H)=\operatorname{Tr}_U(gH).
 \tag{2}
\]
The indices on \(W_H\) refer to the original first head. All
prescribed crossing scalars already in \(W_H\) remain in \(H,C_a\).
The original opened head has no additional pivot.

Split the remaining tensor once more as \(U=V\otimes Z\).
Write \(E_Z,K_Z\) for the ordered generators on the last \(r-1\)
heads, with \(E_Z=0,K_Z=1\) if \(r=1\). Then
\[
                  E=E_VK_Z+E_Z,\qquad K=K_VK_Z.
 \tag{3}
\]
Use \(\iota_a:Z\to U\) and \(\pi_a:U\to Z\) for inclusion
and projection at occupation \(a\) of this first remaining head.
They are different from the endpoints defining \(C_a\).
Define the explicit observer
\[
                   \mathcal B=\iota_d K_Z^{-d}\pi_0.
 \tag{4}
\]
All occupation bases have their coefficient Euclidean metric.

All meridian denominators below are units whenever \(\eta_d\ne0\),
in particular on each strict scaled collar \(|N\mu|<\eta<\pi\).
In fact, with its removable value at zero,
\[
 D_N(M)=\frac{M^N-M^{-N}}{M-M^{-1}},\qquad
                \eta_d=(-1)^dD_N(M),\qquad D_N(1)=N.
 \tag{5}
\]
To verify (5), take \(M^{-d}\) out of the product in (1), use
\(\prod_{j=1}^{N-1}(M^2-Q^j)=(M^{2N}-1)/(M^2-1)\), and
\(Q^{-N(N-1)/2}=(-1)^d\). The zeros of \(\sinh(N\mu)\)
are outside the stated collar except for its removable zero.

## 2. The exact nilpotent adjoint integral

H gives the full capped expression
\[
 C_d=\frac{(-1)^dK^{-d}}{\eta_d}
                  \prod_{j=0}^{d-1}(Q^jL_E-R_E)H,
 \tag{6}
\]
where \(L_E X=EX\), \(R_E X=XE\). These two multiplication
operators commute. At the primitive root, the polynomial identity
\[
 \prod_{j=0}^{d-1}(Q^jX-Y)
             =(-1)^d\sum_{k=0}^dQ^{-k}X^kY^{d-k}
 \tag{7}
\]
holds for commuting \(X,Y\). Indeed
\({d\brack k}_Q=(-1)^kQ^{-k(k+1)/2}\); substituting this in
the finite quantum binomial expansion gives (7). This argument
uses only the nonzero factors \(1-Q^j\), \(1\le j<N\), and
applies at even and composite levels as well.

Since \(gE^k=Q^kE^kg\), (6),(7) give
\[
 \boxed{\quad
 C_d=\eta_d^{-1}\sum_{k=0}^d E^k(gH)E^{d-k}
      =\frac{(-1)^d}{D_N(M)}
                         \sum_{k=0}^d E^k(gH)E^{d-k}.
 \quad}\tag{8}
\]
This is an actual finite nilpotent integral. The relation \(E^N=0\)
includes every physical cap and holds throughout the fixed-root
meridian family. Telescoping (8) proves \([E,C_d]=0\), precisely
the terminal first-column equation. More generally the sum in (8),
as a map of \(gH\), annihilates ordinary \(E\)-commutators.
It is not a positive conditional expectation or a unital projection.

## 3. A physical operator partition with no frame cost

The crucial identity is
\[
 \boxed{\qquad
             \sum_{k=0}^d E^{d-k}\mathcal B E^k
                                  =\eta_d I_U.
 \qquad}\tag{9}
\]
Here is a proof retaining the actual endpoints. Apply L's finite
lowering frame to the split (3). For \(0\le b\le d\), put
\[
 h_b=e_d e_{d-1}\cdots e_{d-b+1},\qquad
 S_E\iota_{d-b}=h_b^{-1}E^b\iota_dK_Z^{-b}.
 \tag{10}
\]
This is triangular with identity diagonal and satisfies
\[
       E=S_E(E_VK_Z)S_E^{-1},\qquad [S_E,K]=0.
 \tag{11}
\]
The top lowering row in (11) follows from the actual \(E^N=0\);
the other rows follow directly from (10). Triangular support gives
the four endpoint identities
\[
 S_E^{\pm1}\iota_d=\iota_d,
                 \qquad \pi_0S_E^{\pm1}=\pi_0.
 \tag{12}
\]
Consequently \(S_E^{-1}\mathcal B S_E=\mathcal B\). No norm
bound for \(S_E\) or its inverse is used.

Conjugate the left side of (9) by \(S_E\). For input occupation
\(a\) on \(V\), the factor \(\pi_0(E_VK_Z)^k\iota_a\)
vanishes unless \(k=a\). That sole surviving summand lowers
\(a\) to zero, raises it by \(\iota_d\), and lowers \(d\)
back to \(a\). The two lowering products combine to
\((e_1\cdots e_a)(e_{a+1}\cdots e_d)=\eta_d\).
Its remaining Cartans cancel exactly:
\(K_Z^{d-a}K_Z^{-d}K_Z^a=I_Z\).
Thus the conjugated sum is \(\eta_d I_U\), proving (9).
All indices lie in \(0,\ldots,d\); neither an exterior arrow nor
a completed infinite string has been introduced.

## 4. The original source is the bounded top-column contraction

Ordinary finite trace cyclicity, (8), and (9) yield
\[
 \begin{split}
 \operatorname{Tr}_U(\mathcal B C_d)
 &=\eta_d^{-1}\operatorname{Tr}_U
        \left(gH\sum_{k=0}^dE^{d-k}\mathcal B E^k\right)\\
 &=\operatorname{Tr}_U(gH).
 \end{split}\tag{13}
\]
Equivalently, the exact original pointed source is
\[
 \boxed{\quad
 \Phi_0(W_H)=\operatorname{Tr}_Z
                  \left(K_Z^{-d}\pi_0C_d\iota_d\right).
 \quad}\tag{14}
\]
This is the literal physical corner. It is not a replacement
closing inferred by scalarity after a mark. For an arbitrary
analytic \(H\) commuting with \(K\), H's completion makes (14)
an identity of holomorphic meridian germs. It applies in particular
to the highest block of any actual total braid intertwiner.

At the root, (8) has coefficient \((-1)^d/N\); it is not obtained
by omitting a dimension factor. If there is only one remaining
head, Cartan commutation makes \(H\) diagonal. Every term of
(8) then has the same total lowering \(d\), and direct evaluation
gives the sharper calibration
\[
               r=1:\qquad C_d=|0\rangle\langle d|\,\tau(H)
 \tag{15}
\]
for the entire meridian family. Thus no unspecified nonzero scalar
is hidden in (14). For larger width, the extensive spectator
operator and its original pivot remain in (14).

## 5. Polynomial observer bounds and every true meridian jet

The observer (4) is a physical rank-one arrow tensored with a
diagonal operator. Since every eigenvalue of \(K_Z\) has modulus
\(|M|^{r-1}\), its rank and its three standard norms are exactly
\[
 \begin{split}
 \operatorname{rank}\mathcal B&=N^{r-1},\\
 \|\mathcal B\|&=|M|^{-(r-1)d},\\
 \|\mathcal B\|_{\rm HS}&=N^{(r-1)/2}|M|^{-(r-1)d},\\
 \|\mathcal B\|_1&=N^{r-1}|M|^{-(r-1)d}.
 \end{split}\tag{16}
\]
On \(|N\mu|\le\eta\), the last scalar factor is at most
\(e^{(r-1)\eta}\). Hence, for example,
\[
 |\Phi_0(W_H)|\le e^{(r-1)\eta}
       N^{(r-1)/2}\|C_d\|_{\rm HS},\qquad
 |\Phi_0(W_H)|\le e^{(r-1)\eta}N^{r-1}\|C_d\|.
 \tag{17}
\]
The trace-norm version has no dimensional prefactor. These are
bounds for a specified observer, not improved bounds for the map
\(H\mapsto C_d\).

Put \(b=(r-1)d\). The sole meridian dependence of the observer is
\(\mathcal B_\mu=e^{-b\mu}\mathcal B_0\). Therefore every fixed
true derivative is given exactly by
\[
 \boxed{\qquad
 \partial_\mu^k\Phi_0(W_{H(\mu)})
     =\operatorname{Tr}_U\left(
             \mathcal B_\mu(\partial_\mu-b)^k C_d(\mu)\right).
 \qquad}\tag{18}
\]
In particular the original first normal is
\[
 \Phi_0'(0)=\operatorname{Tr}_U(\mathcal B_0 C_d'(0))
                                     -(r-1)d\Phi_0(0).
 \tag{19}
\]
Every derivative of the actual \(E,K,H\) in (8) is retained in
\(C_d'(0)\). No derivative of a root symbol substitutes for it.

Writing \(u=N\mu\), the shifted derivative in (18) is
\(N^k(\partial_u-b/N)^k\). Thus (16) gives polynomial cost for
all fixed true jets. Alternatively buffered Cauchy estimates on
\(|u|\le\eta<\eta'<\pi\) bound those jets by \(C_kN^k\) times
the supremum of the actual \(C_d\) norm on the larger collar,
with the same polynomial dimensional factors as (17).
A separately prescribed scalar line multiplies (14); its ordinary
Leibniz derivatives must also be retained. No bound for an arbitrary
external scalar line is implicit in (16).

## 6. What this identifies at the reciprocal endpoint

The reciprocal ordinary column has initial coefficient
\(\widehat\Psi(0)=C_d\). Formula (14) identifies the original
source as one bounded, explicitly marked contraction of that
endpoint. For \(r=1\), (15) says the endpoint coefficient itself
is exactly the original source times a fixed physical arrow.
Accordingly a nonzero estimate for that endpoint cannot be supplied
for free by changing from an ordinary output to a factorial output.

For general width, a large norm of \(C_d\) does not bound its
prescribed contraction from below. The observer is bilinear and
is not a positive density. A local phase/unit estimate for the
whole column also does not determine the spectator trace in (14)
or its competing-region currents. The theorem identifies a missing
source boundary interface; it proves no volume-conjecture case,
geometric cycle coefficient, or arbitrary-short-component lower bound.

Complete proof directs:

* **H:** notes/research_physical_highest_block_endpoint_coordinates.md,
  453 lines, SHA256
  deaadaa899cdb08aefbbcb1e1ca87a40f84a1ade608fceeeaba6426027bd9b1b.
* **L:** notes/research_lowest_physical_block_cut_pairing.md,
  327 lines, SHA256
  be1d3960c0144b69308879d710076b5037e3253ac2ea4b0f788f28616c47d90f.

Only written mathematics and text operations are used. Frozen notes
and public manuscripts are unchanged. The entire matching final was
freshly read nontruncated after the last changes. Complete L was
freshly whole-read in this author sequence; the genuine complete H
whole read was retained fresh and unchanged from the immediately
preceding ordinary-column author sequence. Every used implication
was checked and all three pins were renewed. Independent matching
review and parent adoption remain separate.
