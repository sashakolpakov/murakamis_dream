# The actual unfolded atom requires its cyclotomic divisors and second nome

Research proof, 27 October 2026. The original unfolded Ward factorial
is not horizontal in a rank-one meromorphic line at the physical
parameter origin. Its cyclotomic singularities already accumulate
there. A two-nome difference-period object cancels the local root
pole and has an exact cyclic/source factorization, but it also does
not become an ordinary meromorphic line at the origin. It has
explicit accumulating zeros on another parameter ray.

The positive result is a whole exceptional-slope evaluation of the
actual Ward atom, including its Kummer norm character, and an exact
two-nome root formula retaining the original cyclic gauge and
Heisenberg period. No published analytic-continuation or quantum
dilogarithm proof is a premise.

Use H=Log Q throughout. The physical root is H_N=2pi i/N.
The earlier ADO parameter h=Log q is H/2. A fixed-root normal
epsilon=H-H_N is a different parameter from the varying H_N.

## 1. The function is fixed by the actual Ward jets

The literal finite source has
f_N(z)=sum_(j=0)^(N-1) z^j/(Q_N;Q_N)_j. Its all-level
rational-coefficient unfolding was proved uniquely to be

\[
 F(Q,z)=\sum_{j\ge0}\frac{z^j}{(Q;Q)_j},\qquad
 F(Q,Qz)=(1-z)F(Q,z),\quad F(Q,0)=1.
\]

For |Q|<1, |z|<1, coefficient comparison or iteration gives

\[
 F(Q,z)=\frac1{(z;Q)_\infty},\qquad
 \log F(Q,z)=\sum_{m\ge1}\frac{z^m}{m(1-Q^m)}.       \tag{1}
\]

These are the actual unfolded source functions of
[the Ward construction](unfolded_ward_factorial_and_regulator.md),
not an unrelated function chosen for its growth. The finite nilpotent
head itself only uses the first N coefficients; scalar root values
with nonnilpotent z require the retained central/source data below.

## 2. Cyclotomic singularities exclude the strict meromorphic-line target

Fix a primitive n-th root zeta and Q=zeta exp(epsilon). On a
closed sector around the negative real epsilon ray, uniformly for
|z|<=r<1 with n FIXED,

\[
 \log F(\zeta e^\epsilon,z)
 =-\frac{\operatorname{Li}_2(z^n)}{n^2\epsilon}
      +\log D_n(z)-\frac12\operatorname{Log}(1-z^n)+O(\epsilon),
 \quad D_n(z)=\prod_{j=1}^{n-1}(1-\zeta^jz)^{j/n}.  \tag{2}
\]

All marks start at z=0. Here is an analytic justification of the
coefficient calculation already recorded in the Ward note. Separate
m divisible by n in (1). Nonresonant denominators are uniformly
bounded away from zero on the stated sector: for m|epsilon| small,
use the distance of the finitely many nontrivial n-th roots from
one; otherwise their radial modulus gives a uniform bound. Their
termwise difference from epsilon=0 is O(m|epsilon|), so the z-series
remainder is O(epsilon). For the resonant terms use

\[
 \frac1{1-e^u}=-\frac1u+\frac12+O(u)
\]

uniformly on the same negative sector. For large u the error bound
O(|u|) still holds; summing against r^(kn) justifies the uniform
remainder. The weighted finite-root sum gives the displayed D_n
constant. Thus (2) is a genuine sectorial estimate, not merely a
formal Laurent calculation.

For fixed 0<z<1, every H_(m,n)=2pi i m/n, gcd(m,n)=1, has the
nonzero polar logarithm in (2). Along epsilon=-t,
log|F|=Li_2(z^n)/(n^2t)+O(1). These singularities accumulate at
H=0. A nonzero horizontal frame of a meromorphic rank-one H-line
would be holomorphic and nonzero at every sufficiently small
H_(m,n)!=0, a contradiction. Finite ramification does not help.
A fixed algebraic/Puiseux gauge has only finite-order behavior
there and cannot cancel this exponential singularity. Removing
only exp(-Li_2(z)/H) also leaves every nonzero cyclotomic point
unchanged as a singularity.

This disproves automatic applicability of the strict one-variable
meromorphic-line criterion to the original UNFOLDED ATOM. It does
not prove that singularities cannot cancel in a completed whole
word or selected period; that cancellation would need its actual
source theorem.

## 3. The actual norm is an exceptional normal-slope evaluation

Retain U independently and form the WHOLE ratio

\[
              R(Q,z,U)=F(Q,zU)/F(Q,z).              \tag{3}
\]

The bare generic restriction U=1 is one. Instead put
Q=zeta_n exp(epsilon), U=exp(t n epsilon). For fixed n, t in a
compact subset of C, and |z|<=r<1, the same sectorial argument gives

\[
 \log R(Q,z,U)=t\operatorname{Log}(1-z^n)+O(\epsilon),
 \qquad R\longrightarrow(1-z^n)^t.                 \tag{4}
\]

Proof. Nonresonant terms in the difference of (1) tend to zero
uniformly. For m=kn the term is
z^(kn)(exp(tkn^2 epsilon)-1)/[kn(1-exp(kn epsilon))], whose limit
is -t z^(kn)/k. Uniform Taylor bounds near zero and exponential
bounds away from zero, absorbed into a slightly larger r<1,
justify the summed O(epsilon). This proves (4).

At the ACTUAL slope t=1, U=Q^n and Ward iteration gives EXACTLY

\[
 R(Q,z,Q^n)=(z;Q)_n,\qquad R(Q_n,z,1)_{slope=1}=1-z^n. \tag{5}
\]

Thus the original finite cyclic norm is an exceptional normal-slope
value, not the result of first imposing U=1 generically. It retains
factors such as 1+M^n when they arise from the actual z substitution.

For rational t=a/b, b>0, retain the telescope

\[
 \prod_{j=0}^{b-1}R(Q,zU^j,U)=F(Q,zU^b)/F(Q,z).
                                                               \tag{6}
\]

Here U^b=Q^(an), so for a>=0 the right side is the finite product
(z;Q)_(an), and negative a gives its specified reciprocal product.
Its root value is (1-z^n)^a. The marked individual exceptional
period nu therefore satisfies nu^b=(1-z^n)^a, with nu=1 at z=0.
Equation (6) does NOT assert R^b equals that finite product away
from the exceptional restriction: its arguments are different.

This is a fixed-n sectorial exceptional period and Kummer norm
statement. It is not a holomorphic regular extension across an
entire complex blowup neighborhood, where other cyclotomic
divisors still accumulate. No fixed-n limit is interchanged with
a growing-n limit.

## 4. A two-nome flat difference object made from exact products

Let z=e^x and define, for Re H<0,

\[
 Q=e^H,\quad \widetilde Q=e^{4\pi^2/H},\quad
 y=e^{2\pi i x/H},\quad w=\widetilde Q y,
\]
\[
 \Psi(H,x)=\frac{(w;\widetilde Q)_\infty}{(z;Q)_\infty}
           =\frac{F(Q,z)}{F(\widetilde Q,w)}.         \tag{7}
\]

Both nomes have modulus<1. The numerator product is entire in w;
the log-series quotient is used on the smaller common chart |w|<1.
Elementary product cancellation proves the exact two transports

\[
 \Psi(H,x+H)=(1-z)\Psi(H,x),\qquad
 \Psi(H,x+2\pi i)=(1-y)\Psi(H,x).                   \tag{8}
\]

The two shifts commute, since each multiplier is fixed by the
other shift. In whole independent coordinates (Q,Qtilde,z,y),
the automorphisms are z->Qz and y->Qtilde^(-1)y, respectively.
Equations (8) are a rank-one flat algebraic DIFFERENCE presentation
over that fixed finite-type base. The product (7) supplies one
marked horizontal period. It is not thereby an algebraic section
or an ordinary meromorphic differential line in H.

The second factor is invariant under x->x+H. It is a genuine
difference-constant for the original Ward equation. On the left
upper H sector, x->-infinity along the real axis makes both z,w
tend to zero, specifying the product mark Psi->1. That extra
period/source datum must not be inferred from the first equation
alone.

## 5. Exact physical-root value and the full source factor

Now fix N and H=H_N+epsilon, H_N=2pi i/N. Write X=z^N and mark
V=Log(1-X), nu=(1-X)^(1/N). The exact normal identities are

\[
 \widetilde H=4\pi^2/H+2\pi iN,
 \quad\frac1{\widetilde H}
        =\frac1{N^2\epsilon}+\frac1{2\pi iN},
 \quad w=Xe^{\gamma\widetilde H},\quad
 \gamma=1-x/(2\pi i).                              \tag{9}
\]

For x in a compact marked subset of Re x<0, use (2) on the
numerator atom and its n=1 case on the dual atom. The entire
negative Laurent part of the two logarithms is the same simple
pole -Li_2(X)/(N^2 epsilon), and cancels. Their exact constant
difference gives the sectorial root value

\[
 \boxed{\ \Psi_N(x)=D_N(z)
    \exp\!\left(\frac{\operatorname{Li}_2(X)}{2\pi iN}\right)
                    (1-X)^{x/(2\pi i)-1}.\ }        \tag{10}
\]

For clarity the dual constant is
-Li_2(X)/(2pi iN)+(gamma-1/2)V; subtracting it from
log D_N- V/2 proves (10), including its sign. The estimate is
O(epsilon) on the stated sector. This establishes the finite
marked root value, not an unproved holomorphic H-extension around
the whole root.

Use the ACTUAL determinant-normalized cyclic source gauge

\[
 g_{D,N}=D_N/\nu^{(N-1)/2},\quad
 S(X)=\operatorname{Li}_2(X)+(Nx)V.
\]

Then the COMPLETE factorization is

\[
 \boxed{\ \Psi_N=g_{D,N}\,
       \exp(S(X)/(2\pi iN))\,\nu^{-(N+1)/2}.\ }      \tag{11}
\]

Every determinant root, its half-power mark, and the logarithmic
period is retained. In the actual cyclic Ward substitution
z=-t e one has X=-kappa_N t^N, so 1-X=1+kappa_N t^N is exactly
the original norm, not an arbitrarily dropped central factor.

The source/transport check is decisive. Under x->x+H_N, g_D
multiplies by (1-z)/nu, while S changes by 2pi i V. Their factors
in (11) combine to 1-z, exactly (8). Under x->x+2pi i, g_D
returns to itself and S changes by 2pi iN V, giving 1-X. Thus
the n-step quotient is precisely the finite product (5), with its
central norm and branch marks still present.

The raw finite polynomial also retains its affine source:

\[
 f_N(Q_Nz)-(1-z)f_N(z)=z^N/N.                      \tag{12}
\]

On the nilpotent quotient z^N=0, (11) has central factor congruent
to one and g_D reduces to f_N. This is a canonical projection in
the logarithmic z-jet ring: the Log z terms first occur with z^N.
It is not a literal evaluation of Log of a nilpotent matrix.
For moving tensor sources or nonzero central norm, (11)--(12)
must be retained. Nilpotent-jet agreement does not prove that the
two-nome completion preserves the actual whole normal source.

The formula has the established rational quantum-dilogarithm
coverage described in
[the existing finite/continuous torsor note](rational_quantum_dilogarithm_torsor.md).
Its proof here is the exact original Ward product and the two
normal identities (9), without adopting that literature's proof.

## 6. The completion still is not an ordinary meromorphic H-line

Fix real x<0. The function (7) has exact SIMPLE zeros

\[
                  H_k=(x-2\pi i)/k\longrightarrow0. \tag{13}
\]

Indeed Re H_k<0, both nomes have modulus<1, and w(H_k)=exp(2pi i k)=1.
Only the numerator's first factor 1-w vanishes; the remaining
product and the denominator are nonzero, since |Q|,|Qtilde|,|z|<1.
Moreover w'(H_k)!=0. This proves simplicity directly. A nonzero
horizontal frame of a rank-one meromorphic line at zero cannot
have these accumulating interior zeros. A fixed algebraic Puiseux
gauge cannot remove them. Thus the completion does NOT repair
the strict one-parameter criterion globally either.

This does not prevent a finite polar ASYMPTOTIC along the physical
positive-imaginary sequence. On a fixed marked compact annulus
0<rho<=|z|<=r<1, the actual finite sum for log D_N and elementary
trapezoid bounds give

\[
 \log D_N(z)=-\operatorname{Li}_2(z)/H_N
                         -\tfrac12\operatorname{Log}(1-z)+O(1/N).
\]

The central factor in (10) is exponentially small in its logarithm
on this chart, because X=z^N. Therefore

\[
 \log\Psi_N(x)=-\operatorname{Li}_2(z)/H_N
                         -\tfrac12\operatorname{Log}(1-z)+O(1/N). \tag{14}
\]

For a direct proof of the leading integral, expand
integral_0^1 t Log(1-z exp(2pi it))dt=-Li_2(z)/(2pi i);
the endpoint correction is the displayed -Log(1-z)/2. Uniform
derivative bounds on |z|<=r give the error. This is a statement
about the specified root sequence and chart, not an ordinary
meromorphic H-germ or a global geometric-knot norm.

## 7. The usable target for the whole-period program

The strict selected meromorphic-line polar-character theorem remains
a valid sufficient condition. It cannot be inferred from the actual
local q-factorial atom: both its original and completed forms give
explicit obstructions. The natural exact local target instead keeps
the cyclotomic divisors, the independent power/normal direction of
(3)--(6), the two-nome difference presentation (8), and the central
Heisenberg/norm-root period (11).

The completion is not permission to replace the already selected
Kashaev source by a convenient periodic factor. It has the same
finite nilpotent jets but additional difference-constant period data.
A knot comparison must carry those data, every peripheral factor,
the actual internal projectors and its selected contraction. No
topological invariant, global source descent, or volume conjecture
is proved by this local construction.

[Exact source identities and high-precision root/zero audit](../experiments/audit_unfolded_atom_two_nome_source.py).

The audit passes at 80 decimal digits: 21 fixed-root expansions,
24 exceptional-slope limits, nine exact rational-slope telescopes,
four generic two-nome shift pairs, 14 physical-root constants with
both marked source transports, 12 exact finite-field affine-source
polynomials, six accumulating simple zeros, and 12 independently
bounded physical-root sequence cases. The two normal-coordinate
identities in (9) also pass symbolic verification. The
[saved results](../experiments/unfolded_atom_two_nome_source_results.json)
record every case. These finite checks support the proofs above;
they do not assert uniformity in growing n for the fixed-n normal
limits.

[Independent proof audit](unfolded_atom_two_nome_independent_audit.md)
checks the sectorial estimate, full root constant, norm-root power,
two transports, accumulating simple zeros and trapezoid endpoint.
