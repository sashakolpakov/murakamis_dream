# A source-preserving polynomial-cost filling of a simple transfer seam

28 October 2026. In the ORIGINAL coherently summed physical crossing,
a transfer-clock-one seam can be filled on its zero side without
discarding any endpoint residue. The closed half-integer contour can
be extended across a fixed small negative classical-transfer collar.
All newly enclosed cotangent poles are canceled by actual factorial
zeros. The entire added collar has polynomial pointwise size relative
to its retained zero-transfer kernel, polynomial contour length, and
an exponentially suppressed far edge.

This is a LOCAL exact source operation on regular bulk head charts.
It does not make that zero-transfer exterior small, remove a retained
integer residue at k=0, or bound simultaneous physical/factorial
collisions. It supplies a controlled replacement for a simple artificial
normal endpoint, not a sharp whole-knot estimate.

The subsequent [projected operator completion](actual_projected_transfer_cot_completion.md)
retains the original physical output Fourier projectors. It extends the
negative normal filling to ALL physical input labels, including the
simultaneous scalar collisions below, with subexponential operator cost.
The sharper scalar far-edge estimate here still requires its displayed
regular chart; it is not transferred to unrestricted exteriors.

## 1. Exact kernel and the required regular chart

Use N>=2, d=N-1, Q=exp(2pi*i/N), x=-exp(-pi*i/N) and the EXACT
factorial Fhat_N of
[the original interpolation](exact_factorial_interpolation_and_complex_contours.md).
The original positive total-transfer coefficient with its port monomial
is

    K_N(z)=r_0 (c t)^z
        *Fhat(b+z)/Fhat(b) *Fhat(a)/Fhat(a-z) /Fhat(z),
    r_0=kappa x^(-a-b)Q^(ab), c=x Q^(-b).              (1)

Every power in (1) has its specified logarithm. At physical integers
a,b,z this is the ORIGINAL coefficient with output(b+z,a-z), including
its source normalization. The exact equality with the same full-Psi
completion is in [the normalization comparison](actual_factorial_full_psi_identity.md).
No bare compact Euler function is substituted outside its valid disk.

Fix a compact set of normalized head variables a/N,b/N in the open
strip 0<Re w<1, with bounded imaginary parts, and a bounded logarithmic
chart for t. Fix a finite imaginary height T>0. Choose epsilon>0 so
small that, for -epsilon N-1<=Re z<=0 and |Im z|<=T, BOTH
(b+z)/N and (a-z)/N stay in a fixed compact substrip of 0<Re w<1.
The finite set of small N can instead be excluded by N>=N_0.

This explicit condition keeps the two outside factorial ratios nonzero
and holomorphic throughout the collar. It is essential. A physical
head at a=0,d or b=0,d is not automatically in this chart.

The same construction works in an arbitrary original word by retaining
independent head/port variables before interpolation. In that network
all dependence on this crossing's total transfer is (1); it is not
permissible first to eliminate neighboring head indices and then assume
their additional z dependence is absent. All other original couplings,
caps, pivots and external factors remain in the exterior.

## 2. A uniform small-normal-factor estimate

For z=-u+i v in the collar, u>=0, set M=ceil(u), nu=z+M.
Then 0<=Re nu<1 and |Im nu|<=T. The exact shift equation gives

    1/Fhat(z)=product_(r=1)^M(1-Q^(z+r))/Fhat(nu).      (2)

On this fixed nu rectangle, the convergent Gamma product gives

    Fhat(nu)=(-2pi*i/N)^nu Gamma(1+nu)(1+O_T(1/N)),
    |1/Fhat(nu)|<=C_T N^(Re nu)<=C_T N.              (3)

Only the upper bound is needed. It is uniform on the closed rectangle:
Gamma(1+nu) has neither a zero nor a pole there. The product remainder
in its defining logarithm is O_T(N^-2), and its explicit Gaussian
factor changes (3) by O_T(1/N).

Each factor in (2) is at most C_T(M+1)/N, since |z+r|<=M+T+1
and M<=epsilon N+2. Hence

    |1/Fhat(z)|<=C N [C_0(M+1)/N]^M.                  (4)

The exact bulk-factorial asymptotic and its proved derivative bounds
give |d_w log Fhat(w)|<=C on the two retained bulk substrips.
Integrating along the segments from b to b+z and a to a-z bounds
their ratios in (1) by exp(C(M+1)). Its explicit Cartan factor and
t^z obey the same bound: Log c and Log t are bounded on the specified
chart. Absorbing these factors into C_1 proves the complete estimate

    |K_N(z)/r_0|<=C N [C_1(M+1)/N]^M.                 (5)

If an explicitly retained finite-mode Gaussian is also present, a
factor exp(A z^2/N+B z), with |A|,|B| bounded, is at most
exp(C(M+1)) on this collar and is absorbed by the same estimate.
Thus neither its connecting horizontal pieces nor the monomial phase
has been omitted from (5). No analogous claim is made when those
logarithms or Gaussian coefficients are unbounded.

Choose epsilon so that 2C_1 epsilon<1/2. Then the ENTIRE added collar
has |K_N|<=C N |r_0| for large N. On the far half-integer edge
Re z=-m-1/2, m=floor(epsilon N), equation (5) gives

    |K_N(z)/r_0|<=C N [C_1(m+2)/N]^(m+1)
                    <=poly(N)exp(-c_epsilon N),           (6)

where c_epsilon>0. This is suppression RELATIVE to the actual retained
r_0 and exterior. An unrestricted exterior may still have a larger
exponential rate; (6) has not assigned it the knot volume.

## 3. Exact closed-contour filling, including the horizontal pieces

Consider the original closed transfer rectangle with vertical edges
-1/2 and d+1/2 and horizontal edges Im z=+/-T. Its density is

    omega_N=pi cot(pi z) K_N(z) dz/(2pi*i).             (7)

Its residues at k=0,...,d are exactly the original finite transfer
terms, with forbidden physical terms zero as proved in
[the endpoint theorem](actual_total_transfer_endpoint_packets.md).
Replace its LEFT edge by Re z=-m-1/2 and extend BOTH horizontal
pieces to that edge. The difference of the rectangles encloses
the integers -1,...,-m and no noninteger cotangent pole.

At each such integer Fhat(z) has a simple pole, so 1/Fhat(z) has
a simple zero. The other two factorial ratios are regular and nonzero
by Section 1. Therefore every new cotangent pole in (7) is REMOVABLE.
The full density is holomorphic throughout the added strip, after
these explicit cancellations, and the two closed contour integrals
are EXACTLY equal. In particular the pole at k=0 remains enclosed;
it has not been deleted by rounding a corner.

There is a quantitative chain estimate as well. On a half-integer
vertical edge |cot(pi z)|<=1. On Im z=+/-T it is bounded by a
constant depending only on T. The added horizontal segments have
total length O(N), and the far vertical segment length 2T. Equations
(5)--(6) therefore give polynomial mass and pointwise cost for the
ENTIRE closed filling and the strictly smaller far normal face.
Pointwise equality in the other variables and Fubini on compact
source pieces preserve every original exterior contraction. No
boundary piece from the two finite-height horizontal connections
has been called zero or put into an unproved error term.

An artificial internal split at k=R is simpler: the two adjacent
rectangles have exactly opposite shared vertical edges. Moving this
interface across an integer moves its actual residue from one piece
to the other with opposite signs. Their TOTAL current is unchanged.
For a sublinear interface width, the operator costs of those actual
residues are subexponential by the endpoint theorem. This paired
statement is distinct from deleting the nonzero sourced Ward current
of either packet separately.

## 4. Precise remaining collision and global scope

The filling resolves a SIMPLE transfer-clock-one boundary while the
other four physical-coefficient factors remain regular. A second
factorial collision can cancel the zero used in Section 3. For example
at b=0 the ratio Fhat(b+z)/Fhat(z) is identically one; at a=d the
factor Fhat(a-z) meets a zero across z=-1, so its reciprocal has a pole.
The scalar density can then retain cotangent poles. This scalar proof
does not remove them. Keeping the ORIGINAL physical output Fourier
projection instead supplies the additional zeros counted in the
[projected completion](actual_projected_transfer_cot_completion.md),
which proves all newly enclosed NEGATIVE cotangent poles removable,
with tame normal operator cost. It still retains every original
nonnegative transfer residue and hence does not discard the full-rate
Markov corners in the endpoint theorem.

The bound is uniform on compact regular head/port charts, not across
those collisions, zero/infinity positions, or arbitrary logarithmic
deck changes. It removes one artificial simple boundary from a
descent construction with polynomial local cost. It does not bound
the mass of a complete global deformation or the rate of a remaining
mixed bulk/endpoint period. Joint collision strata and the original
full clock source remain necessary for a sharp volume theorem.

[Audit](../experiments/audit_actual_total_transfer_endpoint_packets.py):
actual coefficient normal identities, source interfaces and forbidden
transfer zeros; supplementary direct checks of the negative-side
removable poles and finite-height density are recorded there. The
closed contour equality follows from the residue proof above.
