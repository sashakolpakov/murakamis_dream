# The complete transfer with both outside variables free

Private research theorem, 9 November 2026. The complete finite transfer
has its nonzero geometric asymptotic while both boundary variables
vary independently in fixed complex neighborhoods. This follows by
combining the exact local integral with the two complete remainder
bounds. The manuscripts remain unchanged.

## 1. Exact finite source

Fix an eligible complete word in powers three and four, beginning
\(343\), with at least five vertices. Let \(z_*\) be its original
third outgoing coordinate. The incoming variable \(w\) is an ordinary
Newton color; \(Z=e^{-2\pi iz}\) is the retained auxiliary outgoing
coordinate. These are independent outside variables. In particular,
\(z\) is not an ordinary right color.

Put \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_b=(r;r)_b\), and retain
\[
 C_{0,N}(Y,Z)=
   \sum_{j=0}^{D}
       \frac{Y^{-j}(rY;r)_j(rZ;r)_j}{(r;r)_j^2}.
 \tag{1}
\]
With the complete original prefix \(F_{34,N}\), define
\[
 T_N(w,z)=\sum_{b=0}^{D}
       \frac{F_{34,N}(w,r^b)}{P_b}C_{0,N}(r^b,e^{-2\pi iz}).
 \tag{2}
\]
This is the complete two-sector transfer in its exact root-sum
representation. It retains every physical index and the original
normalization. As a polynomial in \(w,Z\), it has separate degree
at most \(D\).

Let \(P(w,z)=\mathcal P_0^+(w,z)\), and let \(A(w,z)\) be the
original coefficient in equation (17) of the local-source theorem
with \(\beta=0\). Its factorial symbols and determinant branch
are unchanged.

## 2. Statement and proof

**Theorem.**
There is a fixed complex bidisk \(V\) about \((-2,z_*)\) such that
at all sufficiently large levels of both parities,
\[
 T_N(w,z)=N^{-2}A(w,z)e^{NP(w,z)}
                    \{1+\varepsilon_N(w,z)\},
 \qquad \sup_V|\varepsilon_N|\le C/N.
 \tag{3}
\]
The function \(A\) is nonzero on \(V\). The error is holomorphic,
and on every fixed smaller bidisk,
\[
 \sup|\partial_w^j\partial_z^k\varepsilon_N|
                    \le C_{j,k}/N
             \qquad(j,k\ge0\text{ fixed}).
 \tag{4}
\]
In particular \(T_N\) is nonzero there eventually, and
\[
 \frac1N\log|T_N(w,z)|
       =\Re P(w,z)+O(\log N/N)
 \tag{5}
\]
uniformly on smaller bidisks.

*Proof.* Define the exact local integral \(I_N(w,z)\) using the
fixed segment in equation (15) of the
[original local-source theorem](research_mixed_three_four_next_local_source.md).
It includes the complete prefix, the original forced polynomial
and the whole following kernel. That theorem proves on a fixed
complex bidisk
\[
 I_N(w,z)=N^{-2}A(w,z)e^{NP(w,z)}
                  \{1+\varepsilon_N^{\rm loc}(w,z)\},
 \qquad \sup|\varepsilon_N^{\rm loc}|\le C/N,
 \tag{6}
\]
with a holomorphic relative error and nonzero coefficient.

Set \(M=\lceil N/2\rceil\), and retain the entire adjoining sum
\[
 R_N^+(w,z)=\sum_{b=M}^{D}
       \frac{F_{34,N}(w,r^b)}{P_b}C_{0,N}(r^b,e^{-2\pi iz}).
 \tag{7}
\]
The [left-remainder theorem](research_mixed_next_left_remainder_complex_extension.md)
proves, for the exact difference
\[
 E_N^-(w,z)=T_N(w,z)-I_N(w,z)-R_N^+(w,z),
 \tag{8}
\]
that \(|e^{-NP}E_N^-|\le Ce^{-\eta_-N}\) on a fixed bidisk,
for some \(\eta_->0\). Corollary 2 of the
[incoming-color outer theorem](research_mixed_next_incoming_color_outer_upper_bound.md)
proves on another fixed bidisk
\[
                   |e^{-NP}R_N^+|\le Ce^{-\eta_+N},
                   \qquad \eta_+=\frac1{4\cdot10^{13}}>0.
 \tag{9}
\]
Both estimates apply to the original finite sums in (2) and (7),
with their stated normalizations and every physical row retained.

Intersect the bidisks, then shrink so that \(A\) is bounded away
from zero. The exact identity (8) gives
\[
 \varepsilon_N
 =\varepsilon_N^{\rm loc}
       +\frac{N^2e^{-NP}}{A}(E_N^-+R_N^+).
 \tag{10}
\]
The added term is \(O(N^2e^{-N\min(\eta_-,\eta_+)})\), hence
\(O(N^{-1})\). This proves (3). Fixed-radius Cauchy estimates
give (4). Nonvanishing and (5) follow directly from (3).
No algebraic error from (6) has been assigned an exponential gap.

## 3. The original incoming ordinary derivatives

Let \(u_L(z)\) be the original left endpoint auxiliary coordinate
on the local geometric branch at \(w=-2\). Equation (21a) of the
local-source theorem proves
\[
 P_w(-2,z)=-\frac{\tan(\pi u_L(z))}{4\pi}\ne0.
 \tag{11}
\]
Consequently (3)--(4) imply, for every fixed \(j\ge0\),
\[
 \left.(-1)^j\partial_w^jT_N(w,z)\right|_{w=-2}
  =N^{j-2}A(-2,z)
       \left(\frac{\tan(\pi u_L(z))}{4\pi}\right)^j
       e^{NP(-2,z)}\{1+O_j(N^{-1})\}.
 \tag{12}
\]
The estimate is uniform on smaller outgoing disks. Indeed the
leading differentiated term puts all \(j\) derivatives on the
exponential through \(P_w\), giving \(N^j(P_w)^j\).
Every other term has at most \(j-1\) powers of \(N\), or contains
a derivative of the holomorphic relative error bounded by (4).
Shrinking once more keeps the coefficient in (11) away from zero.
This differentiates the original ordinary polynomial (2);
no auxiliary-coordinate derivative is substituted for an ordinary
normal.

## 4. Scope

The conclusion supplies the complete conditional transfer
with independent outside variables and its actual incoming
ordinary derivatives. It is not a statement about the whole
ordinary right closing sum. That operation still samples all
outgoing physical values, and needs bounds away from the local
geometric neighborhood.

The reference restrictions are unchanged: a terminal third vertex,
length-four words, and a next vertex of type four are not included.
There is no assertion here of stability under arbitrary short
fillings or of finitely many exceptional assignments.

## Source versions

- Original local integral, action, coefficient and derivative:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.
- Left remainder on a complex bidisk:
  fbdc20aba05f2895e1fada626ff6ea8f26b7c8e6300a76fd6c51bb16b9c6f092.
- Incoming-color adjoining estimate:
  5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49.

No mathematical numerical evaluation is used.
