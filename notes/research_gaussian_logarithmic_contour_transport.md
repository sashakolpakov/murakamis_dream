# Exact logarithmic contour shifts and their boundary currents

Research note, 2 November 2026.

The signed Ward packet has an exact contour interpretation. Translating
the original Gaussian residue contours by a spectral lattice step
produces precisely that packet, provided the spectator is transported
with the residue differential. Several consecutive steps have only the
two end strips as their remaining current. Their size can be bounded
in the original full Hermite norm without multiplying a separate
operator norm at every step.

The spectator here is the actual finite polynomial supplied by the
[original source compiler](research_arbitrary_power_source_compilation.md).
This includes products of arbitrary signed fillings, turns, and free
boundary polynomials after their original contractions. A chosen
nonpolynomial interpolation must not be substituted across the
translated contours without checking its poles and its continuation.
The result below does not identify every possible contour remainder
with the Ward packet.

## 1. The original residue in the logarithmic coordinate

Fix \(N\ge2\), \(D=N-1\), and
\[
 q=e^{\pi i/N},\quad \hbar=2\pi i/N,\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},\qquad
 P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
Let \(f_n\) denote the canonical polynomial of \(r_N^n\), where
the original crossing is \(R=\kappa r_N\), and \(n\) is any signed
integer. Put
\[
 z(x)=e^x+e^{-x},\quad
 x_j=(2j+1)\pi i/N,\quad
 G_n(x)=q^{-nD^2/4}
       \exp\!\left(\frac{n(x-\pi i)^2}{2\hbar}\right).
 \tag{2}
\]
The Gaussian has exactly the values and first logarithmic derivatives
of \(f_n(z(x))\) at the original \(N\) nodes. This is the full
Hermite Gaussian identity, including the simple odd node.
Fractional powers here mean \(q^a=\exp(\pi ia/N)\) with this
fixed logarithm. In particular its constant is not obtained
by taking a principal square root of the numerical value of
\(\kappa\).

Let \(\gamma_j\) be small positively oriented circles about \(x_j\),
with the same radius less than \(\pi/N\), for every integer \(j\).
Write \(\mathcal C=\sum_{j=0}^{D}\gamma_j\). For any polynomial
spectator \(A(z)\), define
\[
 \mathcal I_n(A)=\frac{\eta N^2}{4\pi i}
   \int_{\mathcal C}
       \frac{G_n(x)A(z(x))z'(x)}{P_N(z(x))}\,dx.
 \tag{3}
\]
Then
\[
                  \mathcal I_n(A)=\phi_N(f_nA).
 \tag{4}
\]
Indeed the original dualizing-residue formula is
\(\phi_N(B)=\eta N^2\sum_{P_N(c)=0}\operatorname{Res}_c
B(z)\,dz/P_N(z)\). The map \(x\mapsto z(x)\) covers each
ordinary spectral root twice in the stated logarithmic window.
At the odd simple root \(z=-2\), the single preimage \(x=\pi i\)
has local degree two, so its pulled-back residue is doubled.
Thus the factor \(1/2\) in (3) applies there as well. Replacing
\(f_n(z(x))\) by \(G_n(x)\) preserves every needed residue
because their full prescribed jets agree. This proves (4).

The original unnormalized source is \(\kappa^n\mathcal I_n(A)\).
That scalar has modulus one and will not affect the estimates.
All formulas also hold coefficientwise for spectators valued in a
finite-dimensional algebra, keeping its multiplication order.

## 2. The differential determines the spectator transport

For an integer \(k\ge0\), put \(\sigma=k\hbar\) and define
\[
 \begin{split}
 (\mathcal T_k f)(z(x))
     &=f(z(x+\sigma))+f(z(x-\sigma)),\\
 (\mathcal L_k A)(z(x))
     &=\frac{\sinh(x-\sigma)A(z(x-\sigma))
                  +\sinh(x+\sigma)A(z(x+\sigma))}
             {\sinh x}.
 \end{split}                                             \tag{5}
\]
Both are polynomials in \(z\). For the second assertion, the
numerator is an antisymmetric Laurent polynomial in \(e^x\),
and hence is divisible by \(e^x-e^{-x}\); the quotient is
symmetric. In particular the apparent singularities at
\(\sinh x=0\) are removable.

At the physical root,
\[
 P_N(z(x+\sigma))=P_N(z(x-\sigma))=P_N(z(x)).
 \tag{6}
\]
Both maps therefore preserve the ideal \((P_N)\) and descend
linearly to the full original algebra. They are not multiplicative
maps. Their canonical representatives can be used without changing
the result.

**Proposition 1.** For every pair of polynomial spectators,
\[
              \phi_N(A\,\mathcal T_k f)
                         =\phi_N(f\,\mathcal L_k A).
 \tag{7}
\]
Thus \(\mathcal L_k\), rather than an unweighted shift of \(A\),
is the adjoint for the original Frobenius pairing.

**Proof.** Use \(w=e^x\). The full pulled-back residue functional
is a sum at all roots \(w^N=-1\). The substitution
\(w\mapsto q^{2k}w\) permutes these roots. It preserves the
denominator by (6), while the differential transforms from
\(z'(x)\,dx\) to \(z'(x-\sigma)\,dx\). The two opposite
substitutions give exactly (5). All residues are retained,
including their double-pole terms, so this proves (7) in
the full algebra, not just on its reduced spectrum. \(\square\)

There is also an elementary norm statement. With \(U_j\) the
Chebyshev polynomial of the second kind,
\[
 \mathcal L_k U_j(z/2)
       =2\cos\!\left(\frac{2\pi k(j+1)}N\right)U_j(z/2).
 \tag{8}
\]
This follows by writing
\(\sinh x\,U_j(\cosh x)=\sinh((j+1)x)\).
The polynomials \(U_j(z/2)\) are orthonormal for
\[
             d\mu(z)=\frac{\sqrt{4-z^2}}{2\pi}\,dz,
                         \qquad -2\le z\le2.
 \]
Consequently \(\mathcal L_k/2\) is a contraction in this
norm. In particular
\(\mathcal L_k/2=T_k(\mathcal L_1/2)\), and its norm
does not grow exponentially in \(k\).
This is a convenient auxiliary norm on polynomials; it is
not asserted to be a positive formula for the knot invariant.

## 3. An exact translated-contour identity

For \(k\ge1\), set
\[
 \lambda_{n,k}=(-1)^{nk}q^{nk^2},\qquad
 B_\pm(x)=A(z(x\pm\sigma))z'(x\pm\sigma).
 \tag{9}
\]
Gaussian translation gives the entire identity
\[
       G_n(x+\sigma)+G_n(x-\sigma)
             =2\lambda_{n,k}T_{nk}(z(x)/2)\,G_n(x),
 \tag{10}
\]
where \(T_{-j}=T_j\).
Define the boundary current
\[
 \begin{split}
 E_{n,k}(A)=\frac{\eta N^2}{4\pi i}\bigg[
 &\int_{\mathcal C-(\mathcal C+\sigma)}
                  \frac{G_n(x)B_-(x)}{P_N(z(x))}\,dx\\
 +&\int_{\mathcal C-(\mathcal C-\sigma)}
                  \frac{G_n(x)B_+(x)}{P_N(z(x))}\,dx
                                      \bigg].
 \end{split}                                             \tag{11}
\]
Here subtraction means subtraction of the oriented cycles.
The translated circles are precisely
\(\gamma_j\pm\sigma=\gamma_{j\pm k}\).

**Theorem 2.** The actual original source satisfies
\[
 \boxed{\quad
 \mathcal I_n(\mathcal L_k A)
 -\lambda_{n,k}\mathcal I_n(2T_{nk}(z/2)A)
                         =E_{n,k}(A).
 \quad}                                                   \tag{12}
\]
Equivalently, the current is the full-algebra insertion
\[
 E_{n,k}(A)=
 \phi_N\!\left(A\left\{\mathcal T_k f_n
              -2\lambda_{n,k}T_{nk}(z/2)f_n\right\}\right).
 \tag{13}
\]

**Proof.** Insert (10) into the left Gaussian integral before
making any estimate. In its first term change variables from
\(x\) to \(x+\sigma\), and in its second from \(x\) to
\(x-\sigma\). Equation (6) preserves the denominator, and
the differential and spectator become \(B_-\) and \(B_+\).
The translated cycles are \(\mathcal C+\sigma\) and
\(\mathcal C-\sigma\). Comparing these with the two
untranslated integrals defining \(\mathcal I_n(\mathcal L_kA)\)
gives exactly (11)--(12). Equations (4) and (7) give (13).
No estimate or discarded current occurs in this calculation.
\(\square\)

For \(k=1\) there are just four circles:
\[
 \begin{split}
 E_{n,1}(A)=\frac{\eta N^2}{4\pi i}\bigg[
 &\int_{\gamma_0-\gamma_N}
                  \frac{G_n B_-}{P_N(z)}\,dx\\
 +&\int_{\gamma_D-\gamma_{-1}}
                  \frac{G_n B_+}{P_N(z)}\,dx\bigg].
 \end{split}                                             \tag{14}
\]
This identifies precisely which logarithmic contour remainder
is the signed Ward packet.

## 4. The one-step current is exactly the known endpoint packet

Put \(c_0=q+q^{-1}\), \(\rho=q-q^{-1}\), and
\(\varepsilon=(-1)^n\). The packet computed in
[the signed Ward theorem](research_signed_gaussian_ward_endpoint_packet.md)
is
\[
 W_n=(1-\varepsilon)\Pi_0+
       \frac{n\{D+\varepsilon(N+1)\}}{2\rho}\Xi_0.
 \tag{15}
\]
Theorem 2 proves, for arbitrary original polynomial spectators,
\[
                            E_{n,1}(A)=\phi_N(AW_n).
 \tag{16}
\]
This also follows by evaluating the four circles directly.
At every integer-indexed logarithmic node,
\[
 P_N(z(x_j+\delta))=-N^2\delta^2+O(\delta^4),
 \]
so
\[
 \operatorname{Res}_{x_j}\frac{G_n(x)B(x)}{P_N(z(x))}\,dx
             =-\frac{G_n'(x_j)B(x_j)+G_n(x_j)B'(x_j)}{N^2}.
 \tag{17}
\]
At the two original end nodes the Gaussian value is one and
the derivatives are \(-nD/2,+nD/2\). At the two outside
nodes the values are \(\varepsilon\), and the derivatives
are \(-n(N+1)\varepsilon/2,+n(N+1)\varepsilon/2\).
In the lower pair \(B_-=-\rho A(c_0)\), and in the upper
pair \(B_+=\rho A(c_0)\). In both pairs
the corresponding derivative is
\(\rho^2A'(c_0)+c_0A(c_0)\).
Substitution into (14),(17) gives
\[
 E_{n,1}(A)=
 -\eta\left[
   (1-\varepsilon)\{\rho^2A'(c_0)+c_0A(c_0)\}
   +\frac n2\{D+\varepsilon(N+1)\}\rho A(c_0)
                                                       \right].
 \tag{18}
\]
Thus
\[
 \begin{array}{ll}
 n\text{ even}:&
 E_{n,1}(A)=(-1)^N nN\rho\,A(c_0),\\[1mm]
 n\text{ odd}:&
 E_{n,1}(A)=\eta[-2\rho^2A'(c_0)
                           +(n\rho-2c_0)A(c_0)].
 \end{array}                                             \tag{19}
\]
The derivative term in the odd case is compulsory.

In particular,
\[
 \begin{split}
 |E_{n,1}(A)|&\le2\pi|n|\,|A(c_0)|
                                  &&(n\text{ even}),\\
 |E_{n,1}(A)|&\le\frac{8\pi^2}{N^2}|A'(c_0)|
                  +\left(4+\frac{2\pi|n|}{N}\right)|A(c_0)|
                                  &&(n\text{ odd}).
 \end{split}                                             \tag{20}
\]
After the actual half crossing and geometric turn, the insertion
is exactly the one computed in the signed Ward note, with
its polynomial full Hermite and whole-real-boundary bounds.
No change of the external closure is required to use that identity.

## 5. Many steps leave only end strips

Let \(\|A\|_{\mathcal J}\) be the maximum of
\(|A(c)|+|A'(c)|\) at the distinct double spectral roots,
and of \(|A(-2)|\) at the odd simple root.
For operator-valued spectators use any fixed submultiplicative
norm in the same definition.

**Proposition 3.** For every \(k\ge1\),
\[
 \boxed{\quad
 |E_{n,k}(A)|\le
 2\min(k,N)\{\,|n|(N+2k)+6\,\}\|A\|_{\mathcal J}.
 \quad}                                                   \tag{21}
\]
In particular, all shifts \(1\le k\le N\), including a
fixed fraction of one logarithmic turn, have polynomial
current cost \(O_n(N^2)\) in that exact spectator norm.

**Proof.** The first cycle difference in (11) consists
only of the original nodes lost at one end and the new
nodes gained at the other. It has \(2\min(k,N)\) circles.
The other difference has the same count. All overlapping
interior circles cancel with their original orientations.
This is why iterating a norm estimate for a single-step
operator is unnecessary.

Every node that remains has index between \(-k\) and
\(D+k\). On these imaginary logarithms,
\[
 |G_n(x_j)|=1,\qquad
 |G_n'(x_j)|\le |n|(N+2k)/2 .
 \]
At the argument shifted back by \(\pm\sigma\), the spectral
value is again one of the original roots. Since
\(|z'|\le2\) and \(|z''|\le2\) there,
\[
 |B_\pm|\le2\|A\|_{\mathcal J},\qquad
 |B_\pm'|\le6\|A\|_{\mathcal J}.
 \]
At the odd simple root the derivative of \(A\) is not
needed: its coefficient in
\(B_\pm'=(z')^2A'+z''A\) is exactly zero.
Apply (17), multiply each residue by the prefactor
\(\eta N^2/2\) in (11), and sum the at most
\(4\min(k,N)\) circles. This proves (21). \(\square\)

The estimates are independent of the number or form of spectator
factors once their actual product norm is specified. They do not
assert that this product norm has the filled geometric rate.

The full logarithmic turn gives an instructive exact check:
\[
 E_{n,N}(A)=2\{1-(-1)^n\}\mathcal I_n(A).
 \tag{21a}
\]
Indeed \(\mathcal L_N=2I\), \(\lambda_{n,N}=1\), and
\(T_{nN}(z/2)=T_n(T_N(z/2))=(-1)^n\) in the full
quotient \(P_N=0\). Thus the total current vanishes for
even Gaussian power, whereas for odd power it is four
times the original normalized source. A polynomial norm
bound cannot justify deleting that latter current.
One may retain an odd half crossing separately and use
an even Gaussian exponent, as in the earlier source
convention; this is an exact different factorization,
not a reason to drop individual terms in (11).

## 6. Exact removal of a vertex current in the original network

The endpoint functional can be evaluated before estimating its
spectators. This gives a useful exact reduction of the restored
network. Recall its original kernels
\[
 K_T(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w),\qquad
 K_I(z,w)=\sum_{j=0}^{D}e_j(z)e_{D-j}(w).
 \]
Put \(\sigma=(-1)^N=-\eta\).
For each incident edge define two coupons at its other endpoint:
\[
 \begin{array}{c|cc}
       &B_e(w)&C_e(w)\\ \hline
 K_T   &1&T\Pi_0(w)\\
 K_I   &e_D(w)&\Pi_0(w).
 \end{array}                                             \tag{22}
\]
They satisfy the exact endpoint identities
\[
 K_e(c_0,w)=B_e(w),\qquad
 \rho^2\partial_zK_e(c_0,w)=\sigma C_e(w)-c_0B_e(w).
 \tag{23}
\]
For the first, \(e_0(c_0)=1\) and \(e_j(c_0)=0\) for \(j>0\).
For the second, the full residue gives
\(\phi_N(\Pi_0 F)=\sigma[\rho^2F'(c_0)+c_0F(c_0)]\).
The original identity/turn kernel formulas identify
\(\phi_z(\Pi_0(z)K_e(z,w))\) with \(C_e(w)\).
This proves (23) without changing either kernel normalization.

Let a vertex have \(d\) incidences and let its spectator be
\(A(z)=\prod_{e=1}^dK_e(z,w_e)\). Its one-step current is
\[
 \begin{array}{ll}
 n\text{ even}:&
 \displaystyle E_{n,1}(A)
       =\sigma nN\rho\prod_eB_e(w_e),\\[2mm]
 n\text{ odd}:&
 \displaystyle E_{n,1}(A)
       =2\sum_e C_e(w_e)\prod_{f\ne e}B_f(w_f)
        +\eta\{n\rho+2(d-1)c_0\}\prod_eB_e(w_e).
 \end{array}                                             \tag{24}
\]
This is just (19) with the full product derivative in (23).
Any exterior polynomial independent of the removed variable
multiplies both sides and can then be contracted by its original
traces. Thus every original free variable, crossing scalar and
first normal outside the displayed vertex remains unchanged.

For a circle tree all incidences use \(K_T\). Its even current
is a scalar times the network with that vertex and its incident
edges removed. Its odd current is a sum of that deleted network
and \(d\) such networks with a single \(T\Pi_0\) coupon at the
corresponding neighboring vertex. The remaining components may
then be evaluated separately, with their original powers and
closures. This is an identity of finite sources, including any
remaining boundary polynomials.

All coupons in (22) have polynomial full Hermite norm:
\(\|\Pi_0\|_{\mathcal J}=1\),
\(\|e_D\|_{\mathcal J}=1/(4\sin^2(\pi/N))\),
and the bound for \(T\Pi_0\) is proved in the signed Ward note.
The middle equality follows from
\(e_D(z)=\eta P_N(z)/(N^2(z-c_0))\).
The [logarithmic-factorial representative](research_odd_ward_logarithmic_factorial.md)
also gives \(T\Pi_0\) a logarithmic-size representative on
controlled original angle contours, with its poles and
period defect explicitly retained.

Formula (24) is an exact current removal, not an assertion
that the reduced sources have smaller exponential rates.
That comparison must be made in the actual exterior under
consideration.

For an isolated circle-tree vertex whose neighbors are still
free variables, (24) does immediately give a polynomial bound
on the entire real boundary torus: the even current is bounded
independently of \(N\), and the odd current is \(O_{n,d}(N\log N)\).
These are bounds for the actual unreduced boundary polynomials.
The logarithmic-factorial function can replace a neighboring
\(T\Pi_0\) only inside an original trace in that neighbor's
variable. It is not an equality with the free-boundary polynomial
at arbitrary complex arguments. Its logarithmic complex-contour
bound therefore applies after such traces have been restored.

## 7. What the identity permits, and what remains

The translation current has now been identified for a concrete
family of original contour operations, with the exact transported
spectator, full residues, and a polynomial bound for a whole sequence
of lattice steps. These are genuine logarithmic changes of the
Gaussian source (3), not merely an equation on classical critical
points.

Three qualifications remain essential.

First, the source compiler supplies a polynomial spectator.
If it is replaced on the continuous contour by a factorial,
Fresnel, or logarithmic representative, equality of physical jets
only proves equality of the original residue. It does not make
its analytic continuation periodic or remove its other poles.
The translated-contour argument must then include every additional
crossed pole and any change of branch. The formula above applies
unchanged when that replacement is holomorphic and has the same
transport on the entire required contour domain; this must be
proved for the particular replacement.
The shifts proved here are integer multiples of the
imaginary logarithmic step \(2\pi i/N\). A displacement
in an independent complex direction does not preserve
the denominator in (6), and is not covered by the same
current formula.

Second, (21) is relative to \(\|A\|_{\mathcal J}\).
The exterior may itself have an exponential rate larger than the
desired filled volume. A polynomial current cost does not turn
such a rate into a negligible error. The actual turned packet
also has to remain in its original typed position.

Third, (12) is an exact Ward relation, not a bound for its inverse.
The contractions in (8) control the direct spectator shifts;
they give neither an inverse estimate nor a nonzero selected
period. For example, the two terms on the left of (12) may
have a larger common exponential rate and cancel to the smaller
rate of its right side. No lower bound for the knot invariant
is inferred from these upper estimates.

The new usable conclusions are the exact current identity
(11)--(19) for the actual Gaussian contour translations,
the telescoped full-spectator estimate (21), and the
explicit network current removal (24).

## 8. Reproducing the finite comparisons

Run

```sh
python3 experiments/check_gaussian_logarithmic_contour_transport.py --precision 100 --output repro/results/research-gaussian-logarithmic-contour-transport.json
```

The script compares the original full Newton crossing matrix with
the explicit residues on translated logarithmic windows. The
spectator has unreduced degree \(2N+1\), so the comparison also
checks that no premature degree reduction or loss of normals
is being used. It covers levels \(2\) through \(8\), signed
powers \(-3,-1,0,1,2,3\), and shifts including one full
logarithmic period and a step beyond it. It separately checks
the four-circle formula (19) and the bound (21).

[The saved results](../repro/results/research-gaussian-logarithmic-contour-transport.json)
are finite-precision normalization checks, not substitutes for
the residue proof above.
