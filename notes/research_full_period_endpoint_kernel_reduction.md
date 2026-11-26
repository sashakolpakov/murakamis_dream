# Coherent full-period endpoint bounds for the original edge kernel

Private research note, 16 November 2026. Written proof only; frozen
manuscripts and previously adopted notes are unchanged.

The original kernel at the angular endpoint \(t=\pi\), hence spectral
color \(w=2\), has polynomial bounds in the other real color, including
all fixed mixed spectral derivatives. The proof sums the alternating
low Newton sector by exact physical-row interpolation and retains the
entire high radical. It therefore applies to the original first-normal
closing, not just to its value part. A separate continuation estimate
has exponential rate tending to zero as both angular heights tend to
zero. No full-source lower bound or contour deformation is asserted.

## 1. Original data and direct sources

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 J=\lfloor(N-1)/2\rfloor=D-m,\quad \theta=\pi/N,
 \qquad \eta=(-1)^D,
\]
\[
 s_k=2\sin(k\theta),\quad S_k=\prod_{a=1}^k s_a,\quad S_0=1,
 \qquad c_j=2\cos((2j+1)\theta),
\]
\[
 e_k(z)=S_k^{-2}\prod_{a=0}^{k-1}(c_a-z),\qquad
 K_N(w,z)=\sum_{k=0}^{D}e_k(w)e_k(z).
 \tag{1}
\]
The distinct physical nodes are \(c_0,\ldots,c_J\). They are double
except for \(c_J=-2\) at odd levels, where this last node is simple.
All statements below concern these ordinary polynomials before any
physical quotient is taken.

The directly used sources, read in full at the displayed versions, are:

* [Actual matching-edge root location](actual_matching_edge_racah_root_location.md),
  SHA256 f84b82d7924a0c92ca803bc4834bcb0f18f63cedebf2bd072d41d0545a9f5793.
  Its exact polynomial (1), Jacobi realization and positive matrix shift
  prove that every nonconstant folded row has all roots strictly above \(2\).
* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03.
  Equations (17), (34)--(36) give the exact low/high split and the ordinary
  radical's real-period and complex-height bounds; (2), (10) give the
  original full-normal closing.
* [Last physical-row transport](research_last_physical_row_riccati.md),
  SHA256 a6a79106b81b94f5d163022b056c9c6a51e0cdb4f602f090c9f3401436f87c7d.
  Theorem 1 and (23) bound the actual last row at each fixed real color
  below \(2\), at both parities. This source is used only in Section 5.

The first source proves roots greater than \(2\), not merely greater
than \(c_0\). That stronger conclusion is essential here.

## 2. Exact coherent low-sector interpolation

Define the physical rows \(F_{j,N}(w)=K_N(c_j,w)\), \(0\le j\le J\).
For \(k\le j\), the difference-of-cosines product gives
\[
 \prod_{a<k}(c_a-c_j)=\frac{S_{j+k}}{S_{j-k}},\qquad
 e_k(c_j)=\frac{S_{j+k}}{S_{j-k}S_k^2}.
\]
For \(k>j\), \(e_k(c_j)=0\). Consequently
\[
 F_{j,N}(w)=\sum_{k=0}^j
   \frac{S_{j+k}}{S_{j-k}S_k^4}\prod_{a<k}(c_a-w).
 \tag{2}
\]
This is literally the normalized polynomial in the root-location
source, with the same spectral variable. In particular \(F_{0,N}=1\),
\[
 F_{j,N}(c_0)=1,\qquad
 F_{j,N}(w)=\prod_{\ell=1}^{j}
       \frac{r_{j,\ell}-w}{r_{j,\ell}-c_0},\qquad r_{j,\ell}>2.
 \tag{3}
\]
Thus, including \(j=0\),
\[
              0<F_{j,N}(w)\le1\qquad(c_0\le w\le2).
 \tag{4}
\]

Write the exact ordinary split
\[
 K_N=K_N^{\rm low}+H_N^{\rm rad},\qquad
 K_N^{\rm low}(w,z)=\sum_{k=0}^{J}e_k(w)e_k(z),\qquad
 H_N^{\rm rad}(w,z)=\sum_{r=0}^{m-1}e_{D-r}(w)e_{D-r}(z).
 \tag{5}
\]
Every radical polynomial vanishes at every distinct physical node.
If \(L_{j,N}\) are the cardinal polynomials of degree at most \(J\)
on \(c_0,\ldots,c_J\), ordinary interpolation gives
\[
 K_N^{\rm low}(w,z)=\sum_{j=0}^{J}F_{j,N}(w)L_{j,N}(z).
 \tag{6}
\]
Equation (6) is an exact polynomial identity in both variables. Its
derivatives are ordinary derivatives; no normal is discarded.

Here is a uniform bound on this interpolation at both parities. Put
\(\vartheta_\ell=(2\ell+1)\pi/N\), \(0\le\ell<N\). The numbers
\(2\cos\vartheta_\ell\) fold onto the distinct physical nodes, twice
each except for the odd node \(-2\), which occurs once. For a polynomial
\[
 P(z)=\sum_{k=0}^{J}a_kT_k(z/2),\qquad
       \max_{0\le j\le J}|P(c_j)|\le M,
\]
the finite exponential sum on these \(N\) angles gives
\[
 a_0=\frac1N\sum_{\ell=0}^{N-1}P(2\cos\vartheta_\ell),\qquad
 a_k=\frac2N\sum_{\ell=0}^{N-1}
              P(2\cos\vartheta_\ell)\cos(k\vartheta_\ell)\quad(k>0).
 \tag{7}
\]
Indeed every nonzero cosine frequency needed for orthogonality is
less than \(N\), since \(2J<N\). Hence \(|a_0|\le M\),
\[
 |a_k|\le2M,\qquad
        \sup_{-2\le z\le2}|P(z)|\le(2J+1)M\le NM.
 \tag{8}
\]
This also proves the interpolation estimate without a separately
assumed Lebesgue bound. In particular (4) and (6) imply
\[
 \sup_{c_0\le w\le2,\ -2\le z\le2}
                    |K_N^{\rm low}(w,z)|\le N.
 \tag{9}
\]

## 3. Full endpoint bounds, including mixed normals

**Theorem 1.** For every pair of fixed nonnegative integers \(a,b\),
there is \(C_{a,b}\), independent of \(N\), such that
\[
 \sup_{-2\le z\le2}
       |\partial_w^a\partial_z^b K_N(2,z)|
                 \le C_{a,b}N^{2+2a+2b}.
 \tag{10}
\]
More precisely, the low sector in (10) is bounded by
\[
                   C_{a,b}N^{1+2a+2b},
 \tag{11}
\]
and the high sector by \(C_{a,b}N^{2+2a+2b}\).

**Proof.** The same root product gives a bound on a shrinking complex
disk, not just on a real interval. If \(|w-2|\le2-c_0\), then
\(|r_{j,\ell}-w|\le r_{j,\ell}-c_0\), so \(|F_{j,N}(w)|\le1\).
Cauchy's formula therefore gives
\[
 |F_{j,N}^{(a)}(2)|\le a!(2-c_0)^{-a}\le C_aN^{2a},
 \tag{12}
\]
because \(2-c_0=4\sin^2(\pi/(2N))\ge4/N^2\).
Apply (8) to \((\partial_w^aK_N^{\rm low})(2,z)\), whose physical
values are \(F_{j,N}^{(a)}(2)\). The elementary polynomial Markov
inequality on an interval of length \(L\) bounds the first derivative
of a degree-\(d\) polynomial by \(2d^2/L\) times its sup norm.
For complex polynomials the same bound follows by rotating the
derivative at the point being estimated and taking the real part.
Iteration bounds fixed higher derivatives by the corresponding power.
Applying this on \([-2,2]\) in \(z\) proves (11). No lower bound on
\(r_{j,\ell}-2\) is required.

The full radical source proves
\[
 \sup_{w,z\in[-2,2]}|H_N^{\rm rad}(w,z)|\le m(N-1).
 \tag{13}
\]
Its degree in each variable is at most \(D\). Markov on each real
interval therefore gives the high-sector bound. Add (11) to obtain
(10). The cited radical proof is stated for \(N\ge3\); for \(N=2\),
\[
             e_0=1,\quad e_1(z)=-z/4,\quad K_2(w,z)=1+wz/16,
\]
which verifies all the assertions directly. \(\square\)

Thus a physical first normal in the second color costs only a fixed
power of \(N\); so does a first normal at the endpoint \(w=2\), or any
fixed mixed derivative. This includes the odd simple node by evaluation.
The estimate was obtained after the alternating low sum was contracted.
Taking absolute values of its individual Newton summands is a different
estimate and need not have this zero exponential rate.

## 4. Application to the prescribed full-normal trace

Let \(A\) be an arbitrary ordinary spectator polynomial, or its class in
\(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\). Define its physical seminorm
\[
 \|A\|_{\rm H}=
  \max\left\{\max_{a<m}(|A(c_a)|+|A'(c_a)|),
                  \ |A(-2)|\text{ if }N\text{ is odd}\right\}.
 \tag{14}
\]
The original closing is
\[
 \phi_N(f)=\eta\sum_{a=0}^{m-1}
       \{(4-c_a^2)f'(c_a)-c_af(c_a)\}
          +\mathbf1_{N\text{ odd}}f(-2).
 \tag{15}
\]
The double-node formula is the original source residue. At the odd
simple node, \(P_N'(-2)=N^2\) and \(\eta=1\), which gives its displayed
coefficient from \(\phi_N=\eta N^2[z^D]\operatorname{rem}_{P_N}\).
Apply (10) to the product rule in (15). For every fixed \(a\),
\[
 \left|\phi_N\big((\partial_w^aK_N)(2,z)A(z)\big)\right|
                \le C_aN^{5+2a}\|A\|_{\rm H}.
 \tag{16}
\]
This is a bound for the literal original trace, including both its
value and normal terms. It is coefficientwise in additional free
variables, and their derivatives commute with the identity. For several
independently traced endpoint incidences it can be iterated using the
corresponding full mixed Hermite seminorm of the shared spectator.
The spectator is retained: (16) does not estimate it or assert that
its whole network contribution is small.

## 5. A uniform small-height continuation

For \(r>0\) set
\[
 \rho_r=2\cosh r-2,\qquad x_r=2-\rho_r=4-2\cosh r<2,
\]
\[
 \Psi(x)=\frac2\pi\int_0^{\pi/2}
       \operatorname{asinh}\!\left(\frac{\sqrt{2-x}}2\cot y\right)dy
                         \quad(x<2).
 \tag{17}
\]
**Corollary 2.** For every fixed \(r>0\), there are \(C_r,A_r\) such
that, for every \(N\ge2\), every \(|w-2|\le\rho_r\), and every complex
angle \(u\),
\[
 |K_N^{\rm low}(w,-2\cos u)|
       \le C_rN^{A_r}e^{N\Psi(x_r)+J|\Im u|}.
 \tag{18}
\]
For the actual full-period endpoint displacement \(w=2\cosh h\),
\(0\le h\le r\), this gives the full-kernel bound
\[
 |K_N(2\cosh h,-2\cos u)|
 \le C_rN^{A_r}e^{N[\Psi(x_r)+|\Im u|/2]}
              +m(N-1)e^{D[h+|\Im u|]}.
 \tag{19}
\]
In particular the upper exponential rate tends to zero as \(r\to0\)
and \(|\Im u|\to0\). Constants in (18)--(19) may depend on fixed \(r\);
uniformity as \(r\) shrinks with \(N\) is not asserted. At \(h=0\),
the stronger polynomial endpoint theorem already applies.

**Proof.** The exact root product (3) gives
\[
 |F_{j,N}(w)|\le F_{j,N}(2-|w-2|)\le F_{j,N}(x_r).
 \tag{20}
\]
For sufficiently large \(N\), \(x_r<c_0\). The actual row recurrence
in the last-row source has positive coefficients and starts with
\[
 \frac{F_{j+1,N}(x_r)}{F_{j,N}(x_r)}>1.
\]
Indeed its displayed recurrence (2) inducts this inequality from its
first ratio. Thus all the right sides of (20) are at most \(F_{J,N}(x_r)\).
Theorem 1 of that source gives
\[
                F_{J,N}(x_r)\le C_rN^{A_r}e^{N\Psi(x_r)}.
 \tag{21}
\]
Here the omitted interval from \(J/N\) to \(1/2\) changes the exponent
by \(O(N^{-1})\), at either parity. Only a fixed color below \(2\) is
used. The finitely many remaining levels can be absorbed in the constants.

Apply the exact coefficient formula (7) to the polynomial in (6).
For a complex angle, \(|T_k(-\cos u)|=|\cos(ku)|\le e^{k|\Im u|}\).
The sum of its at most \(J+1\) terms proves (18). The original radical
bound (36) of its source, at \(t=\pi-ih\), is exactly the second term
of (19). This proves the full statement without omitting the high normals.

Finally \(\Psi(x_r)\to0\). For an explicit bound put \(c=\sinh(r/2)\)
and assume \(0<c\le1\). Split the integral in (17) at \(y=c\), use
\[
 \operatorname{asinh}(c\cot y)\le\log(1+2c/y)\quad(0<y\le c),
 \qquad \operatorname{asinh}(c\cot y)\le c\cot y\quad(y\ge c).
\]
Since \(\sin c\ge2c/\pi\), direct integration yields
\[
 \Psi(x_r)\le\frac{2c}{\pi}
   \left(3\log3-2\log2+\log\frac{\pi}{2c}\right)
                      =O(r\log(1/r)).
 \tag{22}
\]
This establishes the stated limiting rate. \(\square\)

Fixed derivatives in \(w\) on a strictly smaller disk than the one in
(18) follow by Cauchy's formula with the larger fixed \(r\). Fixed
spectral derivatives in the other color follow by applying Markov
before (7), at an additional polynomial cost. These observations do
not enlarge the endpoint or small-height domain to a full semicircular
boundary at fixed nonzero height.

The coherent endpoint cancellation and (16) supply an actual boundary
kernel estimate. They do not discard the Laurent primitive, angular
vertical current, alias completion, or any other side term in a full
relative contour identity. A filled-source asymptotic still requires
those original terms to be combined and controlled.
