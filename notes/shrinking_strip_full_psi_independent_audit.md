# Independent defining-integral audit of the shrinking-strip full-Psi estimate

28 October 2026. The full-Psi estimates in Section 5 of
[quantitative regular descent](quantitative_regular_phase_descent.md)
are correct, with the explicit Cauchy-disk qualification below. The
proof uses the defining integral and its exact subtraction formula;
no published asymptotic theorem is assumed. It is a local selected-chart
estimate, not a contour-crossing or whole-source boundary theorem.

## 1. Uniform kernel bound with the width displayed

Use the exact remainder formula independently derived in
[the defining-integral note](literature_state_volume.md#21-a-uniform-complex-remainder-on-an-entire-horizontal-strip):

    log Phi_b(z/(2pi b))=Li_2(-exp z)/(2pi i b^2)+R_b(z),
    R_b(z)=-2i[ integral_0^infinity H_b(t)sin(zt/pi)dt
                         +c arctan(z/pi)]-i pi c,
    c=-b^2/24,
    K_b(t)=[1/sinh(b^2t)-1/(b^2t)]/[4t sinh t],
    H_b(t)=K_b(t)-c exp(-t)/t.                         (1)

The constant and logarithm are the ones fixed by the original upper
indentation and the left-half-plane anchor. In particular R_b(0)=
i pi b^2/24; it is not an adjustable scalar normalization.

For all v>0,

    0<=1/v-1/sinh(v)<=v/6.                            (2)

For 0<v<sqrt(6), the right inequality follows by expanding
sinh(v)(1-v^2/6): the cubic coefficient is zero and every subsequent
coefficient is negative, giving sinh(v)(1-v^2/6)<=v. Above sqrt(6)
it follows already from 1/v<=v/6. Thus (2) is uniform.

It gives |K_b(t)|<=b^2/[24sinh(t)]. For t>=1 this is
O(b^2exp(-t)). For 0<t<=1, uniformly in 0<b<=1,

    K_b(t)=c/t+O(b^2t).

Indeed 1/sinh(v)=1/v-v/6+O(v^3) uniformly for v=b^2t<=1;
substitution gives c/sinh(t)+O(b^6t), followed by
1/sinh(t)=1/t+O(t). Consequently

    |H_b(t)|<=Cb^2                 (0<t<=1),
    |H_b(t)|<=Cb^2exp(-t)           (t>=1).            (3)

For 0<delta<=1, integration yields

    integral_0^infinity |H_b(t)|exp((1-delta/pi)t)dt
                          <=Cb^2/delta.               (4)

This estimate has no dependence on Re z. On |Im z|<=pi-delta,
|sin(zt/pi)|<=exp((1-delta/pi)t), so it controls the integral
in (1) uniformly on the entire horizontal strip.

For the remaining elementary term, put w=z/pi. Both 1+iw and
1-iw have positive real part at least delta/pi. On their principal
branches,

    arctan(w)=[Log(1+iw)-Log(1-iw)]/(2i).

The argument difference is bounded by pi, and the modulus ratio
is between (delta/(2pi))^2 and its reciprocal. These bounds persist
for arbitrarily large Re w. Hence

    |arctan(z/pi)|<=C log(2/delta).                    (5)

Equations (1),(4),(5) prove the absolute uniform estimate

    |R_b(z)|<=Cb^2[delta^(-1)+log(2/delta)],
       |Im z|<=pi-delta, 0<b<=1, 0<delta<=1.           (6)

## 2. The actual half-step for both signs

Set b^2=1/N and h=2pi i/N. The actual positive full function has
the recorded identification

    log Psi_+(z)=log Phi_b(w/(2pi b)),
    w=z-i pi(1+1/N).                                 (7)

For delta<=Im z<=2pi-delta and delta>=2pi/N, the distance of w
to both edges +/-pi is at least delta-pi/N>=delta/2. The argument
in the leading dilogarithm is exactly

    -exp(w)=exp(z-h/2).

Write f(z)=Li_2(exp z) on the selected strip continuation from
Re z negative. Then f'(z)=-Log(1-exp z) and
f''(z)=exp z/(1-exp z). For y separated from 2pi Z by delta/2,

    |1-r exp(iy)|>=[delta/(2pi)](1+r), r>=0.

This follows from |1-r exp(iy)|^2=(1-r)^2+4r sin^2(y/2) and
sin(delta/4)>=delta/(2pi). Thus |f''|<=C/delta
uniformly over all real parts, including on the whole half-step
segment. Taylor's integral remainder and (6) give

    log Psi_+(z)=f(z)/h+(1/2)Log(1-exp z)+O(1/(Ndelta)). (8)

The negative actual function is conjugate-reflected with all branches
anchored in the same way. Reflection changes h to -h, but preserves
the SIGN of the half-logarithm. Therefore both signs satisfy

    log Psi_epsilon(z)
       =Li_2(exp z)/(epsilon h)
         +(1/2)Log(1-exp z)+O(1/(Ndelta)),              (9)

on delta<=epsilon Im z<=2pi-delta. There is no hidden sign change
or N-dependent normalizing constant in (9).

## 3. Derivatives down to the stated Ndelta threshold

There is a small logical qualification when using Cauchy's estimate.
At delta=2pi/N, one cannot simply apply a statement formulated only
for margin >=2pi/N to every point of a disk with a smaller margin.
Instead use the defining-integral proof again.

For a center satisfying the hypotheses of (9), take the complex disk
|z'-z|<=delta/4. Its signed angular margin is at least 3delta/4.
After the ACTUAL half-step (7), its Phi strip margin is at least

    3delta/4-pi/N>=delta/4.                            (10)

Both the integral remainder and the Taylor remainder are therefore
O(1/(Ndelta)) throughout this disk. The remainder in (9) is holomorphic
there with its fixed selected branches. Cauchy's formula now proves
for every fixed integer k>=0,

    |partial_z^k remainder|<=C_k/[Ndelta^(k+1)].        (11)

This proves the derivative assertion without strengthening the
threshold delta>=2pi/N or assuming a fixed strip width.

## 4. Source-chart scope and a harmless Hessian sign correction

These estimates apply to the actual full Psi functions on their
selected logarithmic strips and only to such local charts. A product
estimate for the original network must retain every exponential
N-dependent monomial/Gaussian/window factor in its specified leading
action; rational amplitudes must obey the asserted denominator bounds.
The moment-ray corrections and chart-exit currents are not discarded.
No estimate here crosses a quantum pole, identifies a different sheet,
or bounds a mixed endpoint/bulk period.

One unrelated sign in Section 3 of the descent note needs correction.
For its explicitly written W=sum epsilon Li_2(A)+Z^tCZ/2+linear,

    partial^2 W=C+sum epsilon v v^t A/(1-A),            (12)

rather than a minus sign. The polynomial Hessian N/L norm bound
and every subsequent descent estimate use absolute values, so this
correction changes none of those inequalities.

I found no further error in the strip constants, the half-step
normalization, or the claimed local-chart limitation. The separate
global issue remains estimation of all original exit/boundary currents.
