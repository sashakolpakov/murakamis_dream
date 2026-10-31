# Exact face-sign absorption and its cycle obstruction

Workspace research draft, 31 October 2026. Not approved for publication. Finite-source lemma. This separates a genuine
Z/2 face-character test from a representation or regulator theorem.
It applies to the literal homogeneous marked coefficient, before
introducing physical half-power lifts.

## 1. The three LEFT sign chambers

Use the exact real spectral LEFT summand

    A_rest b^i c^(d-j)
      product_(r<i) alpha_r product_(j<r<m) alpha_r K_(i,j).

Stay away from sampled spectral zeros and from the outermost final
spectral cap. The previously proved continuous-real positivity gives
K_(i,j) coefficientwise nonnegative. Let k be the first index in the
lower half with alpha_k<0. The negative-row suffix is k,...,m-1.
For a strict interval chamber the outside-row signs are:

| Endpoints | Number of negative unused rows | Exponent character |
|---|---|---|
| i<=j<k | m-k | none |
| i<=k<=j | m-1-j | c |
| k<i<=j | (i-k)+(m-1-j) | b+c |

Here “c” means multiplication by (-1)^(n_c), where n_c=d-j;
“b+c” means (-1)^(n_b+n_c), n_b=i. Constants modulo2 have
been moved to the original scalar. Thus the respective incidence
characters in the ordered variables (x,b,c,y) are

    (0,0,0,0), (0,0,1,0), (0,1,1,0).                         (1)

Boundary equalities at a pole are not assigned a chamber by this table.
The RIGHT table follows by the actual row reflection and b/c exchange.
The omitted-half Chebyshev scalar A_rest remains intact. The table
does not replace it by one or discard its two oscillatory modes.

## 2. Necessary and sufficient finite incidence criterion

Fix an actual source chamber where every local sign has been written
as an incidence character epsilon_(e,f), together with its retained
scalar. Form the bipartite incidence graph B:

- one row node e for each original port, with supply d;
- one face node f for each ordinary original face, with target d;
- one edge per allowed local incidence (parallel edges are retained).

Protected incidences have target zero and are removed. Do not create
a new mark or change an ordinary target. Suppose numbers gamma_f and
kappa_e in F_2 solve

    epsilon_(e,f)=gamma_f+kappa_e.                            (2)

Then the exact local variable substitution L_f -> (-1)^gamma_f L_f
absorbs every incidence sign, up to the row scalar (-1)^(kappa_e d).
At the ORIGINAL shared coefficient, their aggregate is the known
constant

    (-1)^[ d sum_(ordinary f)gamma_f + d sum_e kappa_e ].       (3)

Every occurrence of a face uses the SAME gamma_f. Homogeneity gives
the row term, and the original target d gives the face term. All
other exact scalar factors and the original exterior framing remain.

Equation (2) has a solution if and only if the sum of epsilon along
every cycle of B is zero in F_2. Necessity follows by summing (2),
since each row/face potential occurs twice. For sufficiency choose
a spanning forest, prescribe one potential on each component, and
propagate (2) across its tree edges. An extra edge is consistent
exactly when its fundamental cycle sum vanishes. This is a finite
linear criterion; no circle-packing geometry is needed to solve it.

Equivalently, on the full affine integer transportation lattice, the sign is
constant precisely when it vanishes on every alternating integral
cycle direction. A bounded nonnegative fiber at a small level need not
contain every such direction. If chamber inequalities are also imposed, (2)
remains sufficient. It is necessary for a chamber that has relative
interior slack along all the graph cycle directions. We make no
necessity claim after structural zeros remove those directions.

## 3. An actual source with a nontrivial cycle

Take the certified one-end width-three word

    (1,3,2,4,1,3),

with its original first cap mark, protected faces0,1. Its exact quartets
are

    (1,0,4,2), (2,0,5,3), (4,2,6,5),
    (5,3,7,0), (1,4,0,6), (6,5,0,7).                         (4)

Give row3 the strict straddling LEFT character, so its incidence at
face7 has epsilon=1. Give every other allowed incidence character0.
The actual incidence cycle

    row3 -- face7 -- row5 -- face5 -- row3                    (5)

has sign sum1. Therefore no global face signs and row gauges solve
(2). This is not repaired by the fact that the underlying white
sphere is simply connected: B is the SOURCE incidence graph, and
its cycles encode simultaneous original face use.

This example does not assert that this character assignment occurs
at a full shared stationary maximum. It proves that an arbitrary
single post-pole local sign cannot automatically be promoted to a
shared signed-clock choice. In particular the scalar repair c->-c
from the local spectral obstruction is not itself a global theorem.

## 4. What the criterion does and does not restore

When (2) is solvable, the original homogeneous polynomial's phase
characters can be absorbed exactly while retaining both protected
zero targets. This is the appropriate algebraic first check for
a candidate signed-clock stationary chart.

It does NOT by itself prove that the resulting action satisfies all
original physical head equations. The adapter H/(bc)^(d/2) also
requires its recorded square-root/central lifts; the original cup,
cap and unrestricted mark fix those choices. Nor does (2) determine
the spectral derivative of A_rest, the primitive auxiliary meridian
log, or a global relative fundamental chain. In particular a free
critical point of the absolute rate cannot be declared to have zero
peripheral log after deleting these scalar phases.

For a true complex stationary phase, its full head derivatives and
literal Morse equations are the already proved route to the original
group. The present result gives a checkable sign obstruction to one
proposed real-to-complex reconstruction, and an exact polynomial
normalization when that obstruction vanishes. It asserts neither
that every global critical point has trivial sign obstruction nor
that every soluble cocycle yields a contribution to the original cycle.
