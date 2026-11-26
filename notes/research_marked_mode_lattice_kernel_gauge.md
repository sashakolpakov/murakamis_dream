# Lattice-kernel choices and a marked local Fourier coefficient

Private written proof, 15 November 2026.

The actual finite source permits integer character changes of its
sampling kernels. Combined with the factorial chamber atlas, these
changes can give any specified integral geometric frequency a nonzero
local coefficient. They can also give that frequency coefficient zero,
without changing the finite source. Thus this local coefficient test
does not determine the contribution of the original integration cycle.
The exact identities below retain every allowed lattice state, offset,
external factor and subsequent full-Hermite closing.

Constant shifts of the cotangent, their side currents, and the
limitation of universal holomorphic source rewrites are already proved
in the cotangent source atlas. One-sided quadrature and finite shifted
Fourier windows are also existing tools. The point here is their precise
combination with the new factorial cone and its previously marked
geometric frequency. No novelty is claimed for the elementary
sampling-kernel identities themselves.

## 1. The finite source and its exact kernel choices

Fix a level and the actual primitive integer coordinates of a resolved
Newton source, with \(d\ge1\). Let \(S_N\subset\mathbb Z^d\) be its finite allowed
support, with no assumption that it is a rectangle. Its literal
interpolated summand \(I_N(Z)\) includes the original crossing phases,
boundary factors, offsets and normalization. Assume it is holomorphic
on a sufficiently small polydisc about every \(k\in S_N\). This is
exactly the local hypothesis verified by the original supported-source
construction; it does not assert global holomorphy of a rectangular
extension. Let \(\Gamma_N\) be the sum of positively oriented product
circles bounding those polydiscs.

Put \(u=e^{2\pi iZ}\). For every integer \(m\), set
\[
 K_m(Z)=\frac{2\pi i u^m}{u-1}.
 \tag{1}
\]
All these kernels have residue one at every integer. Moreover
\[
 K_m-K_0=2\pi i
 \begin{cases}
 \sum_{r=0}^{m-1}u^r,&m>0,\\
 0,&m=0,\\
 -\sum_{r=m}^{-1}u^r,&m<0.
 \end{cases}
 \tag{2}
\]
The right side is entire in \(Z\), including when negative powers of
\(u\) occur. The cotangent differs from \(K_0\) by the entire
constant \(i\pi\).

For any integer vector \(\mathbf m\), therefore,
\[
 \sum_{k\in S_N}I_N(k)
 =\frac1{(2\pi i)^d}\int_{\Gamma_N}
 I_N(Z)\prod_{j=1}^d K_{m_j}(Z_j)\,dZ_1\cdots dZ_d.
 \tag{3}
\]
This is the multivariate residue theorem on each original polydisc.
Alternatively, expand the difference of two product kernels using
(2). Each term is holomorphic in at least one coordinate and has zero
iterated residue. This proof uses the actual support rather than
enlarging it to an integer box. It works with polynomial exterior
parameters or coefficients in a finite-dimensional boundary algebra.
Applying the original closing functional afterwards preserves the
identity, including all its first normals.

If the actual coordinate is \(Z=Nx+a\), use
\[
 \mathcal K_{m,N,a}(x)=N K_m(Nx+a).
 \tag{4}
\]
It has residue one at \(x=(k-a)/N\), and (2)--(3) hold with
these exact offsets and the corresponding differentials. A bounded
complex offset is not discarded. When offsets or external parameters
vary holomorphically, the small circles may be transported locally
with the nodes; the identity and all its parameter derivatives remain
exact. This does not authorize moving them through an interpolation
pole elsewhere.

## 2. A specified marked mode can be the first mode

The convergent expansions of (1) are
\[
 K_m(Z)=
 \begin{cases}
 -2\pi i\sum_{r\ge0}e^{2\pi i(m+r)Z},&\Im Z>0,\\
  2\pi i\sum_{r\ge0}e^{2\pi i(m-1-r)Z},&\Im Z<0.
 \end{cases}
 \tag{5}
\]
Thus their frequency directions are fixed by the side, whereas the
first frequency is an arbitrary integer.

Use the actual factorial chamber atlas in independent scaled labels
\(x\in\mathbb C^d\). Write its wall factor as
\[
 W_N(x)=\prod_\alpha
 \left(1-e^{\tau_\alpha2\pi i
                  (N\ell_\alpha(x)+a_\alpha)}\right)^{e_\alpha},
 \qquad
 \ell_\alpha(x)=A_\alpha\cdot x+b_\alpha,
 \tag{6}
\]
where \(A_\alpha\in\mathbb Z^d\setminus\{0\}\),
\(b_\alpha\in\mathbb R\), and \(e_\alpha\in\mathbb Z\).
Constant factors are kept separately. Fix the chart center \(x_*\)
and put \(h=\Im x_*\). Choose the pointing vector by the atlas
construction, also including every retained coordinate form \(x_j\):
take a real vector \(w\) not orthogonal to any of the finitely many
gradients of forms that are real at the center, and set
\(v=h+\delta w\) for a sufficiently small fixed \(\delta>0\).
This preserves the signs of the imaginary parts of all nonreal
factorial arguments and all nonreal coordinate forms. Choose
\(\tau_\alpha=\operatorname{sgn}(A_\alpha\cdot v)\) for the
arguments real at the center, keeping the canonical half-plane sign
for each nonreal argument. Then
\[
 \tau_\alpha A_\alpha\cdot v>0,
 \qquad v_j\ne0.
 \tag{7}
\]
Set \(\varepsilon_j=\operatorname{sgn}v_j\). For a sufficiently
small fixed \(s>0\), the point \(x_*+isv\) satisfies
\(\tau_\alpha\Im\ell_\alpha(x)>0\) and
\(\varepsilon_j\Im x_j>0\) for all the required forms. Choose a
fixed one-sided subchart about that point where these inequalities
remain strict. On compact subsets of this subchart their positive
lower bounds imply
\(\tau_\alpha\Im(N\ell_\alpha+a_\alpha)>0\) and
\(\varepsilon_j\Im(Nx_j+a_j)>0\) for all sufficiently large
\(N\), uniformly for bounded offsets. Both (5) and the binomial
series for (6) consequently converge normally there. This specified
side is part of the hypothesis; an arbitrary vector satisfying (7)
alone does not supply it at a previously fixed chart center.

**Proposition 1.** For every specified \(\lambda\in\mathbb Z^d\),
choose
\[
 m_j=\begin{cases}\lambda_j,&\varepsilon_j=+1,\\
                  \lambda_j+1,&\varepsilon_j=-1.
       \end{cases}
 \tag{8}
\]
In the Fourier expansion in \(e^{2\pi iNx_j}\), the coefficient
at frequency \(\lambda\) of
\(W_N\prod_j\mathcal K_{m_j,N,a_j}\) is exactly
\[
 c_{\lambda,N}
   =(-2\pi iN)^d\left(\prod_j\varepsilon_j\right)
                      e^{2\pi i\sum_j\lambda_j a_j}\ne0.
 \tag{9}
\]
Every other frequency differs from \(\lambda\) by a vector with
strictly positive pairing with \(v\).

**Proof.** The first term of each kernel in (5) has the chosen
frequency \(\lambda_j\), coefficient
\(-2\pi iN\varepsilon_j e^{2\pi i\lambda_j a_j}\), and subsequent
increments \(r\varepsilon_j e_j\), \(r\ge0\). The wall factor
has constant coefficient one. Every nonconstant wall choice has
increment \(r\tau_\alpha A_\alpha\) with positive pairing with
\(v\). Hence only the tuple of all first kernel terms and constant
wall terms reaches frequency \(\lambda\). This proves (9).
Normal convergence follows from the finite product of geometric and
integer binomial series on the common side. A fixed frequency receives
only finitely many terms: the positive minimum of the finitely many
generator pairings with \(v\) bounds the sum of their nonnegative
multiplicities. Thus grouping frequencies is justified even with
inverse wall factors and dependent affine forms. \(\square\)

For the actual marked geometric phase, the atlas records
\(S_{\rm geom}=S_{\rm chamber}+2\pi i(\lambda\cdot x+\gamma)\),
including earlier adapter characters and their exact offset factors.
When that frequency is integral and the specified common-side
construction applies after the retained wire identifications, (9)
gives a nonzero coefficient for that same
mark; it does not rename another mode as geometric. The associated
constant \(e^{-2\pi iN\gamma}\) and offset constants stay in the
amplitude. The normalized holomorphic remainder of the factorial
atlas is kept as an amplitude, not Fourier-expanded or assigned an
integer coefficient. Fixed complex affine constants require the
common-side hypothesis separately, just as in the atlas. Any wall factor
that becomes constant under those identifications stays outside (6).
If that scalar vanishes, (9) does not remove its zero or give a nonzero
coefficient for the complete product.

The positive-prefix theorem supplies the absence of the macroscopic
gate sine divisors, and hence the atlas charts. Neither it nor (9)
supplies the integration cycle through the resulting local saddle.

## 3. The same finite period also admits a zero local coefficient

Already for the original cotangent kernels, on the same side put
\(u_j=e^{\varepsilon_j2\pi i(Nx_j+a_j)}\). Then
\[
 \pi N\cot\pi(Nx_j+a_j)
   =-i\pi N\varepsilon_j\frac{1+u_j}{1-u_j},
\]
\[
 \pi N\{\cot\pi(Nx_j+a_j)+i\varepsilon_j\}
   =-2i\pi N\varepsilon_j\frac{u_j}{1-u_j}.
 \tag{10}
\]
They differ by an entire constant and give the same exact supported
source in (3). Multiplying by the pointed wall factor (6), the product
of the first kernels has constant Fourier coefficient
\((-i\pi N)^d\prod_j\varepsilon_j\); the product of the second
has constant coefficient zero. In the latter case every term has
strictly positive pairing with \(v\).

The same statement holds at an arbitrary specified frequency. Starting
with (8), replace one \(m_j\) by \(m_j+\varepsilon_j\). Its first
frequency moves from \(\lambda\) to
\(\lambda+\varepsilon_j e_j\). All further increments have positive
pairing with \(v\), so frequency \(\lambda\) is absent. Equation
(2) still preserves the very same finite source. Therefore (9) is
a permissible local normalization, not a gauge-invariant nonvanishing
certificate for that period.

If a supplied contour deformation expresses the original product
cycles as a sum of saddle pieces, endpoints and other currents, apply
the complete kernel difference to that entire identity. Its total
original residue is zero. The contributions of that difference on
the deformed pieces must consequently sum to zero, with any crossed
interpolation poles retained. They need not vanish on the individual
pieces. No decay at infinity, smallness of side currents or global
holomorphy of the source is part of (2). The existing cotangent atlas
proves this qualification for general chart changes and gives its
universal holomorphic-hull limitation. Nothing here evades it.

## 4. Derivative residues require a corrected kernel

There is an additional distinction when a kernel itself represents
Hermite jets rather than ordinary wire sampling. In the unscaled
coordinate define
\[
 H_r(Z)=\frac{(-1)^r}{r!}\partial_Z^rK_0(Z),\qquad
 H_{r,m}(Z)=\frac{(-1)^r}{r!}\partial_Z^rK_m(Z).
 \tag{11}
\]
Their common principal part at an integer is
\((Z-k)^{-r-1}\), so either has residue
\(f^{(r)}(k)/r!\) after multiplication by a holomorphic \(f\).
Their difference is entire by (2). Leibniz's formula gives the exact
correction
\[
 H_{r,m}(Z)=e^{2\pi imZ}
     \sum_{j=0}^r\frac{(-2\pi im)^{r-j}}{(r-j)!}H_j(Z).
 \tag{12}
\]
For a first normal it is
\[
 H_{1,m}=e^{2\pi imZ}(H_1-2\pi imK_0).
 \tag{13}
\]
Simply multiplying the double-pole kernel by the character would
add \(2\pi imf(k)\) to its normal residue. The lower-order term
in (13) cancels it. Tensor products of (11) preserve every prescribed
mixed jet by the same local residue argument. Coordinate changes use
their actual Jacobians and the ordinary chain rule.

Proposition 1 concerns simple wire-sampling kernels. It does not
assert nonvanishing of every differentiated kernel coefficient:
differentiating a Fourier mode can annihilate its constant term.
In the actual Newton construction one may use (3) for the independent
wire indices and leave the original full-Hermite closing untouched.
That procedure preserves every closing normal without modifying its
trace kernel. If a derivative-kernel representation is used instead,
(12), rather than a bare character multiplication, is compulsory.

## 5. Integer coefficients under the literal integral hypotheses

Suppose additionally that every \(b_\alpha\), every factorial offset
\(a_\alpha\), and every sampling offset \(a_j\) is an integer.
Keep the affine integer forms, chamber integers and chosen kernel
frequencies fixed. After removing the displayed common cotangent or
one-sided-kernel factor, every fixed Fourier coefficient of the wall
factor times those simple kernels is an integer independent of the
level. Indeed its factors are integer binomial series and geometric
series, with coefficients \(1\) or \(2\) for the normalized
cotangent. The affine constants and offsets exponentiate to one.
The pointed-cone proof above makes each coefficient a finite signed
sum over integer multiplicities, even when some factors are inverted.
Consequently a nonzero such normalized coefficient has modulus at
least one. This does not say that it is nonzero.

Fixed complex exterior constants and half-offset coordinates need not
satisfy these hypotheses; their phases cannot be dropped. Nor does
this integrality apply to the holomorphic factorial remainder, a
Gaussian determinant, differentiated kernel coefficients with their
additional powers of \(2\pi i\), or the final integrated invariant.

## Sources and scope of verification

The directly used written implications are the actual supported
small-circle construction, the local factorial cone and geometric
mark, and the existing exact kernel/side-current identities. The
following source versions were read without using their computational
appendices:

| Source | Used implication | SHA256 |
|---|---|---|
| [Exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md) | Section 5: original finite support and local holomorphic residue summand | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| [Corner Newton source](research_corner_newton_source_transport.md) | Section 7: actual resolved Newton source, high-index boundary factors, full supported cycle | 24a7f6f721d0a925405424d9a8aba1ac9db8ce7e90ddb937b2a317e10f98b345 |
| [Factorial chamber atlas](research_newton_factorial_chamber_atlas.md) | Sections 3--5: exact gate wall factors, common cone and retained geometric frequency | 34d6e0e4e82a98bf8e6063558ecafdedb0a58d6229fbe462e7e4bfff48f4db4c |
| [Cotangent source atlas](actual_unimodular_cot_source_atlas.md) | Sections 1, 3--5: entire constant shifts, compulsory side currents and universal-transport limitation | cd31da2da36aefb15a4064c3c37198ca03dd6031698e749c30c3ee2d8a99d402 |
| [One-sided wire formula](research_terminal_one_sided_wire_formula.md) | Section 1: original one-sided kernel and all horizontal/vertical corrections | efccbb5a0cf9527c474dc9ab0ac99ae3ea2e53dadfde6edb62a1b6dec70728e6 |
| [Finite Fourier packets](finite_mode_source_quadrature_and_long_twists.md) | Sections 1 and 3.1: shifted finite mode windows and retained endpoint terms | c192956dcd7a97bca9dfa05bf6b53b1c180fda60c014e20dcc1ea27d53b9b59f |

The new conclusions are exact local kernel identities and their
compatibility with the factorial atlas. No numerical evidence,
mathematical code, tests or compilation are used. The original
geometric cycle coefficient and a lower bound for arbitrary fixed
short fillings remain unproved by these operations.
